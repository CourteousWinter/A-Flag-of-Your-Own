"""Map the issue form's OA field to one effort label; never execute issue text."""
import json
import os
from pathlib import Path
import re
from urllib.parse import quote
from urllib.request import Request, urlopen

OPTIONS = {
    'Da stimare': 'effort:unestimated',
    '0.5 OA': 'effort:0.5', '1 OA': 'effort:1', '2 OA': 'effort:2',
    '4 OA': 'effort:4', '8 OA': 'effort:8',
    'Da dividere (>8 OA)': 'effort:split',
}
EFFORT_LABELS = set(OPTIONS.values())


def effort_label(body):
    matches = re.findall(r'^### Stima \(OA\)\r?\n[ \t]*\r?\n([^\r\n]+)', body or '', re.MULTILINE)
    if len(matches) != 1:
        return 'effort:unestimated'
    return OPTIONS.get(matches[0].strip(), 'effort:unestimated')


def synchronize(issue, request):
    """Read live state, add the desired label, remove only obsolete managed labels."""
    desired = effort_label(issue.get('body'))
    current = {label['name'] for label in issue.get('labels', [])}
    if desired not in current:
        request('POST', '/labels', {'labels': [desired]})
    for label in sorted((current & EFFORT_LABELS) - {desired}):
        request('DELETE', '/labels/' + quote(label, safe=''))
    return desired


def main():
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
    repository = os.environ['GITHUB_REPOSITORY']
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Invalid repository name')
    if event['repository']['full_name'] != repository:
        raise ValueError('Event repository mismatch')
    number = int(event['issue']['number'])
    endpoint = f'https://api.github.com/repos/{repository}/issues/{number}'

    def request(method, suffix='', payload=None):
        req = Request(endpoint + suffix, method=method,
                      data=json.dumps(payload).encode() if payload is not None else None,
                      headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                               'Accept': 'application/vnd.github+json',
                               'X-GitHub-Api-Version': '2022-11-28',
                               'Content-Type': 'application/json'})
        with urlopen(req, timeout=30) as response:
            content = response.read()
            return json.loads(content) if content else None

    # Live GET avoids applying an obsolete body from a queued edited event.
    label = synchronize(request('GET'), request)
    print(f'Issue #{number}: {label}')


if __name__ == '__main__':
    main()

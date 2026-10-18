import unittest
from sync_issue_effort import OPTIONS, effort_label, synchronize


class EffortTests(unittest.TestCase):
    def test_all_form_values_and_line_endings(self):
        for value, expected in OPTIONS.items():
            for newline in ['\n', '\r\n']:
                with self.subTest(value=value, newline=newline):
                    body = newline.join(['### Stima (OA)', '', value, '', '### Altro', '', 'note'])
                    self.assertEqual(effort_label(body), expected)

    def test_missing_unknown_and_ambiguous_values_need_triage(self):
        for body in [None, '', '4 OA', '### Stima (OA)\n\n$(anything)',
                     '### Stima (OA)\n\n16 OA',
                     '### Stima (OA)\n\n1 OA\n\n### Stima (OA)\n\n2 OA']:
            with self.subTest(body=body):
                self.assertEqual(effort_label(body), 'effort:unestimated')

    def test_reestimate_preserves_unrelated_labels(self):
        calls = []
        issue = {'body': '### Stima (OA)\n\n4 OA',
                 'labels': [{'name': name} for name in ['bug', 'priority:P1', 'effort:2', 'effort:unestimated']]}
        synchronize(issue, lambda *args: calls.append(args))
        self.assertEqual(calls, [('POST', '/labels', {'labels': ['effort:4']}),
                                 ('DELETE', '/labels/effort%3A2'),
                                 ('DELETE', '/labels/effort%3Aunestimated')])

    def test_repeated_event_is_idempotent(self):
        calls = []
        issue = {'body': '### Stima (OA)\n\n2 OA', 'labels': [{'name': 'effort:2'}]}
        synchronize(issue, lambda *args: calls.append(args))
        self.assertEqual(calls, [])

    def test_failed_add_does_not_remove_previous_estimate(self):
        calls = []
        def fail(method, suffix, payload=None):
            calls.append(method)
            raise RuntimeError('API unavailable')
        issue = {'body': '### Stima (OA)\n\n4 OA', 'labels': [{'name': 'effort:2'}]}
        with self.assertRaises(RuntimeError):
            synchronize(issue, fail)
        self.assertEqual(calls, ['POST'])


if __name__ == '__main__':
    unittest.main()

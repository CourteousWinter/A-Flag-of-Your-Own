import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / 'Editor/run_smoke_test.py'
SPEC = importlib.util.spec_from_file_location('run_smoke_test', MODULE_PATH)
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class SmokeReportTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='afyo-smoke-report-')
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / 'result.json'
        self.project = Path(self.directory.name) / 'AFlagOfYourOwn.uproject'
        self.result = {'run_id': 'current', 'project': str(self.project),
                       'status': 'passed', 'errors': []}

    def write(self):
        self.path.write_text(json.dumps(self.result), encoding='utf-8')

    def read(self, engine_exit=0):
        return RUNNER.read_result(self.path, 'current', self.project, engine_exit)

    def test_current_successful_report_is_accepted(self):
        self.write()
        self.assertEqual(self.read(), self.result)

    def test_missing_or_incomplete_report_is_rejected(self):
        with self.assertRaises(ValueError):
            self.read()
        self.path.write_text('{"run_id":', encoding='utf-8')
        with self.assertRaises(ValueError):
            self.read()

    def test_successful_report_from_previous_run_is_rejected(self):
        self.result['run_id'] = 'previous'
        self.write()
        with self.assertRaisesRegex(ValueError, 'this run'):
            self.read()

    def test_malformed_report_schema_is_rejected(self):
        for value in [None, [], 'passed', {'run_id': 'current'},
                      {'run_id': 'current', 'project': None}]:
            with self.subTest(value=value):
                self.path.write_text(json.dumps(value), encoding='utf-8')
                with self.assertRaises(ValueError):
                    self.read()

    def test_report_from_another_project_is_rejected(self):
        self.result['project'] = str(self.project.with_name('Other.uproject'))
        self.write()
        with self.assertRaisesRegex(ValueError, 'different project'):
            self.read()

    def test_engine_failure_overrides_passed_report(self):
        self.write()
        with self.assertRaisesRegex(ValueError, 'code 7'):
            self.read(engine_exit=7)

    def test_failed_validation_is_rejected_even_when_engine_exits_zero(self):
        for change in [{'status': 'failed'}, {'errors': ['missing map']}]:
            with self.subTest(change=change):
                self.result.update(change)
                self.write()
                with self.assertRaises(ValueError):
                    self.read()
                self.result.update(status='passed', errors=[])


if __name__ == '__main__':
    unittest.main()

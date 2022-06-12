import unittest
from unittestreport import TestRunner
from common.hande_path import CASES_DIR,REPORT_DIR

suite = unittest.defaultTestLoader.discover(CASES_DIR)

runner = TestRunner(suite,
                    filename='report.html',
                    report_dir=REPORT_DIR
                    )

runner.run()




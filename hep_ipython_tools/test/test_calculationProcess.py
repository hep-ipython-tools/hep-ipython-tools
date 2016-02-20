from time import sleep
from unittest import TestCase

from hep_ipython_tools.calculation_process import CalculationProcess
from hep_ipython_tools.calculation_queue import CalculationQueue
from hep_ipython_tools.test.fixtures import MockQueue

class DerivedCalculationProcess(CalculationProcess):
    def start_process(self, **kwargs):
        self.result_queue.put("TestItem", "TestValue")
        self.result_queue.put("AnotherTestItem", "AnotherTestValue")

class OngoingCalculationProcess(CalculationProcess):
    def start_process(self, **kwargs):
        while True:
            sleep(1)


class TestCalculationProcess(TestCase):
    def get_terminated_process(self):
        queue = CalculationQueue()
        process = DerivedCalculationProcess(result_queue=queue, log_file_name=None, parameters=None, process_kwargs=[])
        process.start()
        process.join()
        return process

    def test_invalid_result_queue(self):
        self.assertRaises(ValueError, DerivedCalculationProcess, result_queue=None,
                          log_file_name=None, parameters=None, process_kwargs=None)

    def test_default_parameters(self):
        queue = CalculationQueue()
        process = DerivedCalculationProcess(result_queue=queue, log_file_name=None, parameters=None, process_kwargs=[])

        self.assertFalse(process.is_alive())
        self.assertTrue(process.is_valid)

    def test_get_keys(self):
        process = self.get_terminated_process()

        keys = process.get_keys()

        self.assertIn("TestItem", keys)
        self.assertIn("AnotherTestItem", keys)

    def test_get(self):
        process = self.get_terminated_process()

        self.assertEqual(process.get("TestItem"), "TestValue")
        self.assertEqual(process.get("AnotherTestItem"), "AnotherTestValue")

        self.assertRaises(KeyError, process.get, "UnknownItem")

    def test_isAlive(self):
        process = self.get_terminated_process()

        self.assertFalse(process.is_alive())

    def test_get_log(self):
        raise NotImplementedError

    def test_save_log(self):
        raise NotImplementedError

class TestOngoingCalculationProcess(TestCase):
    def setUp(self):
        queue = CalculationQueue()
        self.process = OngoingCalculationProcess(result_queue=queue, log_file_name=None, parameters=None, process_kwargs=[])

    def tearDown(self):
        self.process.terminate()

    def test_get(self):
        self.process.start()

        self.assertEqual(self.process.get_keys(), None)
        self.assertEqual(self.process.get("TestItem"), None)
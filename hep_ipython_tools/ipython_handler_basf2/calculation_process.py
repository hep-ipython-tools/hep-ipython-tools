import basf2

from hep_ipython_tools.ipython_handler_basf2 import python_modules
from hep_ipython_tools.calculation_process import CalculationProcess
from hep_ipython_tools.ipython_handler_basf2.entities import Basf2CalculationQueueStatistics


class Basf2CalculationProcess(CalculationProcess):

    """
    Overload implementation of the HEPProcess with the correct handling of the path calculation.
    """

    def __init__(self, result_queue, log_file_name, parameters, path, random_seed=None):
        #: Random seed to set. None will not set it.
        self.random_seed = random_seed
        #: Path to process.
        self.path = path

        super(Basf2CalculationProcess, self).__init__(result_queue=result_queue, log_file_name=log_file_name,
                                                      parameters=parameters)

    def prepare(self):
        """
        A function to prepare a path with the modules given in path.
        """
        if self.path:
            # Append the needed ToFileLogger module
            created_path = basf2.create_path()
            file_logger_module = basf2.register_module("ToFileLogger")
            file_logger_module.param("fileName", self.log_file_name)
            created_path.add_module(file_logger_module)

            # Copy the modules from the path
            for module in self.path.modules():
                created_path.add_module(module)

            # Add the progress python module
            created_path.add_module(python_modules.ProgressPython(self.progress_queue_remote))

            # Add the print collections python module
            created_path.add_module(python_modules.PrintCollections(self.result_queue))

            self.path = created_path

        else:
            self.is_valid = False

    def start_process(self):
        """
        The function given to the process to start the calculation.
        Do not call by yourself.
        Resets the logging system, logs onto console and a file and sets the queues
        (the result queue and the process queue) correctly.
        """

        if not self.path:
            return

        try:
            if self.random_seed is not None:
                basf2.set_random_seed(self.random_seed)

            basf2.reset_log()
            basf2.logging.zero_counters()
            basf2.log_to_file(self.log_file_name)
            basf2.process(self.path)
            self.result_queue.put("ipython.statistics", Basf2CalculationQueueStatistics(basf2.statistics))
        except:
            raise
        finally:
            self.progress_queue_remote.send("end")

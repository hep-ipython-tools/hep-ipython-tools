from hep_ipython_tools.calculation import Calculation
from hep_ipython_tools.simple.calculation_process import SimpleCalculationProcess
from hep_ipython_tools.simple.viewer import VariableViewer


class SimpleCalculation(Calculation):
    def __init__(self):
        super().__init__()

    def show_variable(self, index=None):
        def f(process):
            return VariableViewer(process.some_variable)

        self.create_widgets_for_all_processes(f, index)

    def append(self, result_queue, log_file_name, parameters=None, **kwargs):
        self.process_list.append(SimpleCalculationProcess(result_queue=result_queue, log_file_name=log_file_name,
                                                          parameters=parameters, **kwargs))

from hep_ipython_tools.calculation import Calculation
from hep_ipython_tools.simple.calculation_process import SimpleCalculationProcess
from hep_ipython_tools.simple.viewer import VariableViewer


class SimpleCalculation(Calculation):
    def __init__(self):
        Calculation.__init__(self)

        self._calculation_process_type = SimpleCalculationProcess

    def show_variable(self, index=None):
        def f(process):
            return VariableViewer(process.some_variable)

        self.create_widgets_for_all_processes(f, index)
from hep_ipython_tools.simple.calculation import SimpleCalculation
from hep_ipython_tools.simple.information import SimpleInformation
from hep_ipython_tools.ipython_handler import IPythonHandler


class SimpleIPythonHandler(IPythonHandler):
    def __init__(self):
        super().__init__()

        #: A shortcut for returning information on the basf2 environment.
        self.information = SimpleInformation()

        # Use our own calculation type.
        self._calculation_type = SimpleCalculation

from hep_ipython_tools.simple.calculation import SimpleCalculation
from hep_ipython_tools.simple.information import SimpleInformation
from hep_ipython_tools.ipython_handler import IPythonHandler


class SimpleIPythonHandler(IPythonHandler):

    def __init__(self):
        IPythonHandler.__init__(self)

        #: A shortcut for returning information on the environment.
        self.information = SimpleInformation()

        # Use our own calculation type.
        self._calculation_type = SimpleCalculation

from hep_ipython_tools.basf2.process import Basf2Process
from hep_ipython_tools.ipython_handler import IPythonHandler
from hep_ipython_tools.basf2.information import ModulesInformation, Basf2Information


class Basf2IPythonHandler(IPythonHandler):
    """
    Handler class to start processes in an IPython notebook in a convenient way.
    From this whole framework you should not need to create any instances by yourself but rather use the
    given ipython handler for this.

    Usage
    -----

    Create a handler object in the beginning of your NB and use the two methods `process`
    and `process_parameter_space` to turn a path or a path creator function into a Basf2Calculation.
    Do not create calculations on you own.

        from tracking.validation.ipython_handler import handler

        path = ...

        calculation = handler.process(path)

    """

    def __init__(self):
        """
        Set the basf2 related shortcuts.
        """

        super().__init__()
        #: A shortcut for returning information on the basf2 environment.
        self.information = Basf2Information()

        #: A shortcut for returning module information
        self.modules = ModulesInformation()

    def process(self, path, result_queue=None):
        IPythonHandler.process(self, result_queue=result_queue, path=path)

    def _generate_process(self, result_queue, log_file_name, **kwargs):
        return Basf2Process(result_queue=result_queue, log_file_name=self.next_log_file_name(), **kwargs)

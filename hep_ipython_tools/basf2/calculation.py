from hep_ipython_tools import viewer
from hep_ipython_tools.basf2.process import Basf2Process
from hep_ipython_tools.calculation import Calculation


class Basf2Calculation(Calculation):
    """
    Overloaded class with more functionality which is basf2 specific.
    """
    def show_path(self, index=None):
        """
        Show the underlaying basf2 path in an interactive way
        """
        def f(process):
            if process.path is not None:
                return viewer.PathViewer(process.path)
            else:
                return None

        self.create_widgets_for_all_processes(f, index)

    def get_modules(self, index=None):
        """
        Return the modules in the given path.
        """
        return self.map_on_processes(lambda process: process.path.modules() if process.path is not None else None, index)

    def append(self, result_queue, log_file_name, parameters=None, **kwargs):
        """
        Use the Basf2Process to construct new processes.
        """
        self.process_list.append(Basf2Process(result_queue=result_queue, log_file_name=log_file_name,
                                              parameters=parameters, **kwargs))

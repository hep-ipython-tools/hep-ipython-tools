from hep_ipython_tools import viewer
from hep_ipython_tools.calculation import Calculation


class Basf2Calculation(Calculation):
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

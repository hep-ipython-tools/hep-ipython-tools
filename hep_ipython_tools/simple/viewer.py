from hep_ipython_tools.viewer import IPythonWidget


class VariableViewer(IPythonWidget):

    def __init__(self, some_variable):
        self.some_variable = some_variable

    def create(self):
        from ipywidgets import HTML
        return HTML("""<h1>Title</h1><p>{some_variable}</p>""".format(some_variable=self.some_variable))

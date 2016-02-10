from hep_ipython_tools import viewer


class StylingWidget(viewer.StylingWidget):
    """The css string for styling the notebook."""
    css_string = """
        #notebook {
            background-color: rgba(20, 166, 255, 0.3);
            background-image: url("http://www-ekp.physik.uni-karlsruhe.de/~nbraun/belle.svg");
            background-repeat: no-repeat;
            background-position: right bottom;
        }

        #notebook-container {
            width: 90%;
        }

        #menubar-container {
            width: 90%;
        }

        #header-container {
            width: 90%;
        }
        """


class PathViewer(viewer.IPythonWidget):

    """
    Viewer object for the basf2 path.
    Do not use it on your own.
    """

    def __init__(self, path, standalone=False):
        """
        Create a new path viewer object with the path from the process
        """
        #: The path to show
        try:
            self.path = path.modules()
        except:
            self.path = path

        self.standalone = standalone

    def create(self):
        """
        Create the widget
        """

        import ipywidgets as widgets

        if self.path is None:
            return widgets.HTML("No modules in path.")

        a = widgets.Accordion()
        children = []

        for i, element in enumerate(self.path):
            html = ModuleViewer(element, standalone=self.standalone)
            children.append(html.create())
            if isinstance(html.module.name, str):
                a.set_title(i, html.module.name)
            else:
                a.set_title(i, html.module.name())

        a.children = children

        return a


class ModuleViewer(viewer.IPythonWidget):
    """
    A widget for showing module parameter with their content (not standalone)
    or with their description (standalone).
    """

    def __init__(self, module, standalone=True):
        """ Init with a module as a string or a registered one. """
        if isinstance(module, str):
            import basf2
            self.module = basf2.register_module(module)
        else:
            self.module = module
        self.standalone = standalone

        #: Template for the table beginning
        self.table_beginning_html = """<table style="margin-left: auto; margin-right: auto;
                                       border-collapse: separate; border-spacing: 0px;">"""

        #: Template for the table cell
        self.td_html = "style=\"padding: 10px;\""

        #: Template for the row of parameters
        self.table_row_parameters = """<tr><td {td_style}>{param.name}</td>
                                      <td{color_text} {td_style}>{param.values}</td>
                                      <td style="color: gray; {td_style}>{param.default}</td></tr>"""

        #: Template for the row with help
        self.table_row_help = """<tr><td {td_style}>{param.name}</td>
                                      <td {td_style}>{param.type}</td>
                                      <td {td_style}>{param.values}</td>
                                      <td style="color: gray; {td_style}>{param.description}</td></tr>"""

        #: Template for the simple row
        self.table_row_html_single = """<tr><td colspan="4" {td_style}>{text}</td></tr>"""

        #: Template for the table title
        self.table_title_html = """<thead><td colspan="4" style="text-align: center;
                                   font-size: 18pt;" {td_style}>{module_name} ({package})</td></thead>"""

    def get_color_code(self, param):
        """
         Handy function for getting a color based on a parameter:
         if it has the default value, no color,
         if not, red color.
        """
        if str(param.values) != str(param.default) and str(param.default) != "":
            color_text = " style='color: red;'"
        else:
            color_text = ""
        return color_text

    def create(self):
        """
        Show the widget.
        """
        import ipywidgets as widgets

        html = widgets.HTML()
        html.value = self.table_beginning_html

        if self.standalone:
            if isinstance(self.module.name, str):
                module_name = self.module.name
            else:
                module_name = self.module.name()

            html.value += self.table_title_html.format(module_name=module_name, package=self.module.package(),
                                                       td_style=self.td_html)

            html.value += self.table_row_html_single.format(text=self.module.description(), td_style=self.td_html)

        if len(self.module.available_params()) == 0:
            html.value += self.table_row_html_single.format(text="No parameters available.", td_style=self.td_html)
        else:
            for param in self.module.available_params():
                color_text = self.get_color_code(param)

                if self.standalone:
                    table_row_html = self.table_row_help
                else:
                    table_row_html = self.table_row_parameters

                html.value += table_row_html.format(param=param, color_text=color_text, td_style=self.td_html)
        html.value += "</table>"

        return html
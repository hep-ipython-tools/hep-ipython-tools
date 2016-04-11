from hep_ipython_tools.information import EnvironmentInformation


class SimpleInformation(EnvironmentInformation):

    def __init__(self):
        EnvironmentInformation.__init__(self)

        self.externals_version = "Test"
        self.externals_option = "Test"
        self.option = "Test"
        self.architecture = "Test"
        self.release = "Test"
        self.release_folder = "Test"

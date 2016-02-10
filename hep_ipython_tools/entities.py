class StoreContent:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class ModuleStatistics:

    """
    Dictionary list holding the module statistics (like the C++ class ModuleStatistics)
    """

    def __init__(self, stats, categories):
        #: Name property
        self.name = stats.name
        #: Time sum property
        self.time_sum = self.get_dict(stats.time_sum, categories)
        #: Time mean property
        self.time_mean = self.get_dict(stats.time_mean, categories)
        #: Time std property
        self.time_stddev = self.get_dict(stats.time_stddev, categories)
        #: Memory sum property
        self.memory_sum = self.get_dict(stats.memory_sum, categories)
        #: Memory mean property
        self.memory_mean = self.get_dict(stats.memory_mean, categories)
        #: Memory std property
        self.memory_stddev = self.get_dict(stats.memory_stddev, categories)
        #: Calls property
        self.calls = self.get_dict(stats.calls, categories)

    @staticmethod
    def get_dict(function, categories):
        """
        Call the function on each information in the categories and return a dict
        name -> function(value)
        """
        return {name: function(category) for name, category in categories}


class Basf2CalculationQueueStatistics:

    """
    As the basf2 statistics is not pickable, we can not store it into the queue.
    So we write a wrapper which unpacks the needed properties.
    """

    def __str__(self):
        """ Make the str behave like before """
        return self.str

    def __repr__(self):
        """ Make the repr behave like before """
        return self.str

    def __init__(self, statistics):
        """ Initialize with the C++ statistics """
        #: The module statistics list
        self.module = []

        categories = [("INIT", statistics.INIT),
                      ("BEGIN_RUN", statistics.BEGIN_RUN),
                      ("EVENT", statistics.EVENT),
                      ("END_RUN", statistics.END_RUN),
                      ("TERM", statistics.TERM),
                      ("TOTAL", statistics.TOTAL)]

        for stats in statistics.modules:
            self.append_module_statistics(stats, categories)

        self.append_module_statistics(statistics.getGlobal(), categories)

        #: The str representation
        self.str = statistics()

    def append_module_statistics(self, stats, categories):
        """ Helper function to append modulewise stats """
        self.module.append(ModuleStatistics(stats, categories))
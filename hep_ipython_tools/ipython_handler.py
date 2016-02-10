import os
import tempfile
from abc import abstractmethod, ABCMeta

from hep_ipython_tools import viewer, calculation_queue, calculation, information


class IPythonHandler(metaclass=ABCMeta):

    """
    Handler class to start processes in an IPython notebook in a convenient way.
    From this whole framework you should not need to create any instances by yourself but rather use the
    given ipython handler for this.

    Usage
    -----

    Create a handler object in the beginning of your NB and use the two methods `process`
    and `process_parameter_space` to turn a path or a path creator function into a Calculation.
    Do not create calculations on you own.

        from tracking.validation.ipython_handler import handler

        path = ...

        calculation = handler.process(path)

    """

    def __init__(self):
        """
        Each created log file gets registered and deleted if there are more than 20 log files present
        or if the get_log function of the process is called (the log is saved elsewhere).
        As the log files are saved to /tmp you have probably not to care about deleting them.
        """

        #: A list of open log files.
        self.log_files = []

        #: A shortcut for returning information on the environment.
        self.information = information.EnvironmentInformation()

    @staticmethod
    def style():
        """
        Show a nice styling :-)
        """
        styling_widget = viewer.StylingWidget()
        styling_widget.show()

    def process(self, result_queue=None, **kwargs):
        """
        Turn a path into a Calculation that you can start, stop or whatever you want.

        Arguments
        ---------
        result_queue: The CalculationQueue you want to use. Without giving this as a parameter
           the function creates one for you. Create one on your own with the function create_queue.
        """

        if result_queue is None:
            result_queue = calculation_queue.CalculationQueue()

        created_process = self._generate_process(result_queue=result_queue,
                                               log_file_name=self.next_log_file_name(), **kwargs)

        return calculation.Calculation([created_process])

    def process_parameter_space(self, kwargs_creator_function, **kwargs):
        """
        Create a list of calculations by combining all parameters with all parameters you provide and
        feeding the tuple into the kwargs_creator_function.
        If the kwargs_creator_function has a parameter named queue, the function feeds the corresponding
        created queue into the kwargs_creator_function.
        The kwargs_creator_function must return a dictionary for every combination of parameters it gets,
        which will be used to construct a Process out of it (namely, it will be fet to _generate_process).
        See basf2/ipython_handler for an example.

        Please note that a list of calculations acts the same as a single calculation you would get from
        the process function. You can handle 10 calculations the same way you would handle a single one.

        Arguments
        ---------
        kwargs_creator_function: A function with as many input parameters as parameters you provide.
           If the function has an additional queue parameter it is fed with the corresponding queue for this path.
        list_of_parameters: As many lists as you want. Every list is one parameter. If you do not want a
           specific parameter constellation to occur, you can return None in your kwargs_creator_function for
           this combination.

        Usage
        -----

            def kwargs_creator_function(par_1, par_2, par_3, queue):
                kwargs = {... par_1 ... par_2 ... par_3}
                queue.put(..., ...)
                return kwargs

            calculations = handler.process_parameter_space(kwargs_creator_function,
                                                           [1, 2, 3], ["x", "y", "z"], [3, 4, 5])

        The returned kwargs must fit your _generate_process function!
        """

        calculation_list = calculation.CalculationList(kwargs_creator_function, kwargs)
        all_paths, all_queues, all_parameters = calculation_list.create_all_calculations()

        process_list = [self._generate_process(result_queue=q, log_file_name=self.next_log_file_name(),
                                               parameters=parameters, **kwargs)
                        for kwargs, q, parameters in zip(all_paths, all_queues, all_parameters)]
        return calculation.Calculation(process_list)

    def next_log_file_name(self):
        """
        Return the name of the next log file.
        If there are more than 20 log files present,
        start deleting the oldest ones.
        """
        next_log_file = tempfile.mkstemp()
        self.log_files.append(next_log_file)
        while len(self.log_files) > 20:
            first_log_file = self.log_files.pop(0)
            f = first_log_file[0]
            log_file_name = first_log_file[1]

            os.close(f)
            try:
                os.unlink(log_file_name)
            except OSError:
                pass
        return next_log_file[1]

    @staticmethod
    def create_queue():
        """
        Create a Calculation queue. You need to do this if you want to pass it to your modules
        and write to it while processing the events.
        """
        return calculation_queue.CalculationQueue()

    @abstractmethod
    def _generate_process(self, result_queue, log_file_name, **kwargs):
        """
        Use this function to transform some parameters in kwargs into the real process. The returned object must be
        an instance of HEPProcess. See basf2/ipython_handler for an example.
        """
        pass

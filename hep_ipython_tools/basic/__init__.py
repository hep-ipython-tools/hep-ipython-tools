from hep_ipython_tools.calculation import Calculation
from hep_ipython_tools.calculation_process import CalculationProcess
from hep_ipython_tools.ipython_handler import IPythonHandler


class BasicCalculationProcess(CalculationProcess):
    """
    Overload this class and implement how a calculation should be done in your framework.
    """
    def __init__(self, result_queue, log_file_name, parameters, another_variable):
        """
        Define all other variables you need for your calculation process here.
        In this case, only the another_variable is used, but you can declare as many
        parameters as you like. When calling handler.process or handler.process_parameter_space
        later, you have to give the same variables here (or you give them default values).

        Please make sure to include the result_queue, the log_file_name and the parameters also and hand
        them over to the base calculation process object.

        When the constructor of the base class is called, also the function prepare will be called.
        You can use it to prepare your process before start is actually
        called (maybe to check the validity of the variables before
        start_process is called). For example, you can set the self.is_valid parameter
        to False to indicate that tis particular process will not be processed.
        """
        self.another_variable = another_variable

        CalculationProcess.__init__(self, result_queue=result_queue, log_file_name=log_file_name,
                                    parameters=parameters)

    def start_process(self):
        """
        Do your calculation here.
        Use the variables attached to this calculation process, to steer the calculation.

        This calculation is ran detached from the main process, so make sure to collect all information before.

        The failure of the calculation is handled by the exit code, so set it accordingly.

        The following parameters should be used to communicate with the outside environment:

        * self.progress_queue_remote.send("start"/"end"/percentage) to set the information used
          in the progress bar viewer.
        * Put things onto the self.result_queue, to store them for later usage. You have to give a unique name,
          because later calls to put with the same identifier will overwrite former calls.
          You can use two distinct identifier for writing out the statistics ("ipython.statistics")
          or the collection content ("ipython.store_content").
        * Use the file self.log_file_name to write log information in it. The content of the file will be
          preserved later.

        For a simple use case, see the simple/calculation_process.py.
        """
        pass


class BasicCalculation(Calculation):
    """
    Overloading this class should be very easy in most of the cases, because you just have to declare which
    calculation process type should be used (see the __init__ function for that).
    However, if you want the user to be able to access more information than the basic ones (e.g. your
    customized viewer objects), you can add the methods here. See simple/calculation.py for an example.
    """
    def __init__(self):
        """
        We do nothing more than calling the base constructor and setting the _calculation_process_type
        afterwards to the correct type (our own one).
        """
        Calculation.__init__(self)

        self._calculation_process_type = BasicCalculationProcess


class BasicIPythonHandler(IPythonHandler):
    """
    As this object will be the only entrance point for the user, we have to set the _calculation_type to our
    concrete overloaded class BasicCalculation.

    You can also use this class to declare other general-usage parameters or functions, for example lookup methods
    or information printer functions.
    See simple/ipython_handler.py or ipython_handler_basf2/ipython_handler.py for examples.
    """
    def __init__(self):
        IPythonHandler.__init__(self)

        # Use our own calculation type.
        self._calculation_type = BasicCalculation


# The user should not create a handler instance on his own, so we prepare one.
handler = BasicIPythonHandler()

# Only export the handler and not the basic types.
__all__ = [handler]
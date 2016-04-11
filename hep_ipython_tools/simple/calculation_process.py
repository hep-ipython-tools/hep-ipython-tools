from time import sleep
from hep_ipython_tools.calculation_process import CalculationProcess
from hep_ipython_tools.entities import StoreContent, StoreContentList, Statistics, StatisticsColumn


class SimpleCalculationProcess(CalculationProcess):

    def __init__(self, result_queue, log_file_name, parameters, some_variable):
        #: Some needed variable
        self.some_variable = some_variable

        super(SimpleCalculationProcess, self).__init__(result_queue=result_queue, log_file_name=log_file_name,
                                                       parameters=parameters)

    def start_process(self):
        self.progress_queue_remote.send("start")

        store_content_list = []
        module_statistics = []

        # Mock the process
        for i in range(self.some_variable):
            sleep(1)

            # Mock progress
            self.progress_queue_remote.send(1.0 * i / self.some_variable)

            store_content_list.append(self.get_store_content(i))
            module_statistics.append(self.get_statistics(i))

        # Mock results
        self.mock_log(self.log_file_name)
        self.result_queue.put("ipython.statistics", self.mock_statistics(module_statistics))
        self.result_queue.put("ipython.store_content", self.mock_content(store_content_list))

        self.progress_queue_remote.send("end")

    def mock_statistics(self, module_statistics):
        # Mock statistics
        first_column = StatisticsColumn("First")
        second_column = StatisticsColumn("Second")
        third_column = StatisticsColumn("Third")
        columns = [first_column, second_column, third_column]
        statistics = Statistics(columns=columns, modules=module_statistics)
        return statistics

    def mock_content(self, store_content_list):
        return store_content_list

    def mock_log(self, file_name):
        # Mock log
        with open(file_name, "w") as f:
            f.write("[DEBUG] I have waited %d seconds.\n" % self.some_variable)
            f.write("[WARNING] This is not a real process.\n")
            f.write("[RESULT] I will finish now.\n")

    def get_statistics(self, i):
        # Mock statistics
        return {"First": 10, "Second": 30, "Third": i * 20}

    def get_store_content(self, i):
        # Mock store content
        store_content = [StoreContent("TestVariable", 42)]
        return StoreContentList(store_content, i)

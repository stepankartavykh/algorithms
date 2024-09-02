import cProfile
import inspect
import os
import random
import resource
import time
from resource import getrusage, RUSAGE_SELF
from typing import Iterable
from abc import abstractmethod, ABC
from typing import Callable

DEFAULT_STATS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/stats'


class UsageResource:
    def __init__(self, usage_object: resource.struct_rusage):
        self.usage_object = usage_object
        params = usage_object.__match_args__
        self.params = {param: getattr(usage_object, param)
                       for param in params}


class DataPacket:
    def __init__(self, data):
        self.data = data


class LoadInterface:

    def __init__(self, input_type: type, packets_number: int):
        self._type = input_type
        self.data_packets = []
        self.packets_number = packets_number
        self._generate_input_data()

    @abstractmethod
    def _generate_input_data(self) -> None:
        raise NotImplementedError('Not implemented!')

    @abstractmethod
    def test_workloads(self):
        raise NotImplementedError('Not implemented!')

    @abstractmethod
    def get_data_packets(self) -> Iterable:
        raise NotImplementedError('Not implemented!')


class SpecificInterface(LoadInterface, ABC):

    def _generate_input_data(self):
        for _ in range(self.packets_number):
            self.data_packets.append(DataPacket([random.randint(1, 1000) for _ in range(random.randint(1, 1000))]))

    def get_data_packets(self) -> Iterable:
        for packet in self.data_packets:
            yield packet


class ValidationError(Exception):
    """Error occurs when type of generated data not match input data annotations."""


def watcher(function: Callable):
    def _validate_input_data(function_types, data_input):
        print(function_types, data_input)
        if list(function_types.values())[0].annotation != type(data_input):
            raise ValidationError('Data in input and function types not match!')

    def wrapper(*args, **kwargs):
        print('start collecting info...')
        input_types = dict(inspect.signature(function).parameters)
        try:
            _validate_input_data(input_types, args[0])
        except ValidationError as valid_error:
            print(valid_error)
        # TODO - The question is how to extract valuable info using package 'resource'?
        usage_object_before = getrusage(RUSAGE_SELF)
        print(usage_object_before)
        result = function(*args, **kwargs)
        usage_object_after = getrusage(RUSAGE_SELF)
        print('end collecting info...')
        return result

    return wrapper


class TestClient:
    def __init__(self, approaches: list[Callable], data_load: LoadInterface, stats_dump_path=DEFAULT_STATS_DIR,
                 stdout_print: bool = True, make_dump: bool = False, number_of_datasets: int = 1):
        self.functions = approaches
        self.work_load = data_load
        self.collected_data = []
        self.stats_dump_path = stats_dump_path
        self.stdout_print = stdout_print
        self.make_dump = make_dump
        self.number_of_datasets = number_of_datasets

    def _get_profiling_data(self, func: Callable, print_to_stdout: bool = True, make_dump: bool = False):
        with cProfile.Profile() as profiler:
            func([random.randint(1, 100) for _ in range(self.number_of_datasets)])
            if print_to_stdout:
                profiler.print_stats()
            if make_dump:
                profiler.dump_stats(f'{DEFAULT_STATS_DIR}/{func.__name__}{time.time_ns()}.txt')

    def run(self):
        for approach in self.functions:
            self._get_profiling_data(approach, print_to_stdout=self.stdout_print, make_dump=self.make_dump)
            approach_with_watcher = watcher(approach)
            for input_data_packet in self.work_load.get_data_packets():
                approach(input_data_packet.data)
                approach_with_watcher(input_data_packet.data)

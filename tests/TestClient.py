import cProfile
import os.path
import random
import time
from abc import abstractmethod, ABC
from typing import Callable, Type

DEFAULT_STATS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/stats'


class DataPacket:
    def __init__(self, data):
        self.data = data


class LoadInterface:

    @abstractmethod
    def __init__(self, input_type: type):
        self._type = input_type
        self.data_packets = self._generate_input_data()

    @abstractmethod
    def _generate_input_data(self) -> DataPacket:
        raise NotImplementedError('Not implemented!')

    @abstractmethod
    def test_workloads(self):
        raise NotImplementedError('Not implemented!')

    @abstractmethod
    def get_data_packets(self):
        raise NotImplementedError('Not implemented!')


class SpecificInterface(LoadInterface, ABC):

    def _generate_input_data(self):
        for _ in range(100):
            self.data_packets.append(DataPacket([random.randint(1, 1000) for _ in range(random.randint(1, 1000))]))
        return self.data_packets

    def get_data_packets(self) -> list[DataPacket]:
        return self._generate_input_data()


def watcher(function: Callable):

    def wrapper(*args, **kwargs):
        print('start collecting info...')
        result = function(*args, **kwargs)
        print('end collecting info...')
        return result

    return wrapper


class TestClient:
    def __init__(self, approaches: list[Callable], data_load: Type[LoadInterface], stats_dump_path=DEFAULT_STATS_DIR):
        self.functions = approaches
        self.work_load = data_load
        self.collected_data = []

    @staticmethod
    def get_profiling_data(func: Callable):
        with cProfile.Profile() as profiler:
            func([random.randint(1, 100) for _ in range(1000)])
            profiler.dump_stats(f'/home/skartavykh/MyProjects/leetcode/tests/stats/{func.__name__}{time.time_ns()}.txt')

    def run(self):
        for approach in self.functions:
            for input_data_packet in self.work_load.get_data_packets():
                approach(input_data_packet)


def test_function(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda element: element % 2 != 0)


if __name__ == '__main__':
    test_client = TestClient([test_function], SpecificInterface(list[int]))
    test_client.run()

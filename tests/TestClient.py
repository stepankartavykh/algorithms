import timeit
from typing import Callable


class LoadInterface:
    pass


class TestClient:
    def __init__(self, approaches: list[Callable], data_load: LoadInterface):
        self.functions = approaches
        self.work_load = data_load



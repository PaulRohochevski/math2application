from abc import ABC, abstractmethod
from typing import Tuple


class IMethod(ABC):

    @staticmethod
    @abstractmethod
    def calculate(func, interval: Tuple[int or float, int or float], epsilon: float) -> Tuple[float, int]:
        """
        TODO: Write a description.
        :param func:
        :param interval:
        :param epsilon:
        :return:
        """
        pass

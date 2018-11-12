# coding=utf-8
from typing import Tuple

from . import IMethod


class BisectionMethod(IMethod):

    @staticmethod
    def calculate(func, interval: Tuple[int or float, int or float], epsilon: float) -> Tuple[float, int]:
        """
        TODO: Write a description.
        :param func:
        :param interval:
        :param epsilon:
        :return:
        """
        # Interval values
        a, b = interval

        if func(a) * func(b) > 0:
            raise ValueError("No roots found on INTERVAL {}".format(interval))

        else:
            midpoint: float = None
            cnt: int = 0

            while abs(a - b) >= epsilon:
                midpoint = (a + b) / 2.

                if func(a) * func(midpoint) > 0:
                    a = midpoint

                else:
                    b = midpoint

                cnt += 1

            return midpoint, cnt

# coding=utf-8
from scipy.misc import derivative
from typing import Tuple

from . import IMethod


class NewtonMethod(IMethod):

    @staticmethod
    def calculate(func, interval: Tuple[int or float,], epsilon: float) -> Tuple[float, int]:
        """
        TODO: Write a description.
        :param func:
        :param interval:
        :param epsilon:
        :return:
        """
        # Interval value
        a = interval[0]

        # Function value from 'a'
        f_a = func(a)

        cnt: int = 0

        while abs(f_a) > epsilon:
            try:
                a = a - float(f_a) / derivative(func, a)

            except ZeroDivisionError as zde:
                raise ValueError(zde)

            f_a = func(a)

            if cnt > 100:
                raise ValueError("Too many iterations. Didn't find an answer.")

            else:
                cnt += 1

        return a, cnt

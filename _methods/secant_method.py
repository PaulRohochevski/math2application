# coding=utf-8
from typing import Tuple

from . import IMethod


class SecantMethod(IMethod):

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

        # Function values from 'a' and 'b'
        f_a, f_b = func(a), func(b)

        val: float = None
        cnt: int = 0

        while abs(f_b) > epsilon:
            try:
                denominator = float(f_b - f_a) / (b - a)
                val = b - float(f_b) / denominator

            except ZeroDivisionError as zde:
                raise ValueError(zde)

            a, b = b, val
            f_a, f_b = f_b, func(b)

            if cnt > 100:
                raise ValueError("Too many iterations. Didn't find an answer.")

            else:
                cnt += 1

        return val, cnt

# coding=utf-8
from collections import Counter
from typing import Tuple
from enum import IntEnum
import sys
import re

from _methods import *


class AppMenu(IntEnum):
    """
    TODO: Write a description.
    """
    view_and_enter_values = 1
    calc_using_bisection_method = 2
    calc_using_secant_method = 3
    calc_using_newton_method = 4
    exit = 5


class MathCMDApplication(object):
    __slots__ = ('__find_var', '__func', '__func_str', '__interval', '__epsilon')

    __FIND_VAR_RE_PATTERN: re.compile = re.compile(r'[a-z]+', re.I)

    def __init__(self, use_def_val: bool = False):
        """
        Constructor with default values.
        # TODO: Parse default values from config file
        """
        self.__find_var: str = 'x' if use_def_val else None
        self.__func: function = lambda x: x ** 2 - 7 if use_def_val else None
        self.__func_str: str = 'x^2 - 7' if use_def_val else None
        self.__interval: Tuple[int or float, int or float or None] = (1, 5) if use_def_val else None
        self.__epsilon: float = 0.0001 if use_def_val else None
        print(f"\=====> Numerical Methods <=====/")
        self.__menu()  # Start the application

    @staticmethod
    def __parse_input(input_func):
        """
        TODO: Write a description.
        :param input_func:
        :return:
        """
        try:
            digit: int = int(input(':'))

        except ValueError:
            print("Please, use digits.")

        else:
            input_func(digit)

    def __menu(self) -> None:
        """
        TODO: Write a description.
        :return:
        """
        while True:
            print(f"\n# ===== Menu =====\n"
                  f"# {AppMenu.view_and_enter_values}) View & enter values\n"
                  f"# {AppMenu.calc_using_bisection_method}) Calculate using Bisection Method\n"
                  f"# {AppMenu.calc_using_secant_method}) Calculate using Secant Method\n"
                  f"# {AppMenu.calc_using_newton_method}) Calculate using Newton Method\n"
                  f"# {AppMenu.exit}) Exit")

            self.__parse_input(self.__parse_menu_input)

    def __parse_menu_input(self, value: int) -> None:
        """
        TODO: Write a description.
        :param value:
        :return:
        """
        if value == AppMenu.view_and_enter_values:
            self.__enter_values()

        elif value == AppMenu.calc_using_bisection_method:
            self.__calc(BisectionMethod)

        elif value == AppMenu.calc_using_secant_method:
            self.__calc(SecantMethod)

        elif value == AppMenu.calc_using_newton_method:
            self.__calc(NewtonMethod)

        elif value == AppMenu.exit:
            exit(0)

        else:
            raise ValueError(f"Unexpected value: {value}")

    def __enter_values(self):
        """
        TODO: Write a description.
        :return:
        """
        while True:
            print(f"\n## ===== Current Values =====\n"
                  f"## Function: {self.__func_str if self.__func_str is not None else ''}\n"
                  f"## Interval: {self.__interval if self.__interval is not None else ''}\n"
                  f"## Epsilon: {self.__epsilon if self.__epsilon is not None else ''}\n"
                  f"##\n"
                  f"## ===== You Can Enter New Values =====\n"
                  f"## 1) Set new Function (e.g. x^2 - 7)\n"
                  f"## 2) Set new Interval (e.g. (-1, 3) or (3,))\n"
                  f"## 3) Set new Epsilon (e.g. 0.0001)\n"
                  f"## 4) Back to the menu")

            self.__parse_input(self.__parse_enter_values_input)

    def __parse_enter_values_input(self, value: int) -> None:
        """
        TODO: Write a description.
        :param value:
        :return:
        """
        if value == 1:
            func_str = input('Enter a function: ')
            all_vars = self.__FIND_VAR_RE_PATTERN.findall(func_str)
            if self.__find_var not in all_vars:
                vars_cnt = Counter(all_vars)
                most_common_var = vars_cnt.most_common(1)[0][0]
                self.__find_var = most_common_var

            self.__func = eval(f"lambda {self.__find_var}: {func_str.replace('^', '**')}")
            self.__func_str = func_str

        elif value == 2:
            interval_str = input('Enter an interval: ')
            self.__interval = eval(interval_str)

        elif value == 3:
            epsilon_str = input('Enter an epsilon: ')
            self.__epsilon = float(epsilon_str)

        elif value == 4:
            self.__menu()

        else:
            raise ValueError(f"Unexpected value: {value}")

    def __calc(self, method: (BisectionMethod, SecantMethod, NewtonMethod)):
        """
        TODO: Write a description.
        :param method:
        :return:
        """
        if self.__func is not None:
            if self.__interval is not None:
                if self.__epsilon is not None:
                    try:
                        x, cnt = method.calculate(self.__func, self.__interval, self.__epsilon)

                    except ValueError as ve:
                        print(f"\n>>> {ve}")

                    else:
                        print(f"\n>>> Calculated using {method.__name__} (loops count = {cnt})"
                              f"\n>>> x = {x}")

                else:
                    print('Set an epsilon.')

            else:
                print('Set an interval.')

        else:
            print('Set a function.')


if __name__ == '__main__':
    arg_use_def_val: bool = False

    # TODO: Implement usage of 'argparse' lib
    if len(sys.argv) == 2 and sys.argv[-1] == '--use_def_val':
        arg_use_def_val = True

    m = MathCMDApplication(use_def_val=arg_use_def_val)

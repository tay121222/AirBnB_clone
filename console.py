#!/usr/bin/python3
"""beautiful code that passes the pycodestyle checks"""


class simple_program:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        Print("{}".format(self.value))


def main():
    simple_prog = simple_program(35)
    simple_program.print_value()


if __name__ = "__main__":
    main()

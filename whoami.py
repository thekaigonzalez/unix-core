import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Gives your current user.  """
    b = open('usr/user.txt', 'r')
    name = b.readlines()[0]
    printc(name)
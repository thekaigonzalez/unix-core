import curses




def printw(str: str):
    stdscr = curses.initscr()
    stdscr.addstr(str)
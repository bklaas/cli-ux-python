"""Generic cli UX methods for a richer console-driven experience."""
# import glob
# from pathlib import Path
import sys

from tqdm import tqdm
from colorama import Fore, Style


def pbar(iterable, **kwargs):
    """Wrapper on tqdm progress bar to give sensible defaults.

    Args:
        iterable: a data structure to be iterated with progress bar.
        kwargs: pass-through arguments to tqdm
    Returns:
        tqdm: progress bar with sensible defaults
    """
    defaults = {
        "bar_format": "{l_bar}{bar}|{n_fmt}/{total_fmt} {percentage:3.0f}%",
        "ncols": 80,
        "unit": "files",
        "desc": "Files",
    }
    for k, v in defaults.items():
        if k not in kwargs:
            kwargs[k] = defaults[k]
    return tqdm(iterable, **kwargs)


def traceback_off():
    """Turns off traceback messages on Exceptions."""
    sys.tracebacklimit = 0


def traceback_on():
    """Turns on traceback messages on Exceptions."""
    sys.tracebacklimit = 1000


def redprint(*args):
    cprint(args, color="red")


def greenprint(*args):
    cprint(args, color="green")


def yellowprint(*args):
    cprint(args, color="yellow")


def blueprint(*args):
    cprint(args, color="blue")


def magentaprint(*args):
    cprint(args, color="magenta")


def cyanprint(*args):
    cprint(args, color="cyan")


def whiteprint(*args):
    cprint(args, color="white")


def blackprint(*args):
    cprint(args, color="black")


def cprint(*args, color="black"):
    msg = args
    fg_colors = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    print(fg_colors[color.lower()], end="")
    print(msg)
    print(Style.RESET_ALL, end="")

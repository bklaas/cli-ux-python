"""Generic cli UX classes for a richer console-driven experience."""
import time
import math
from collections import Counter
from .methods import *


class CliUx(object):
    """Collection class for cliux stuff, and things."""

    def __init__(self):
        self.pbar = pbar
        self.traceback_on = traceback_on
        self.traceback_off = traceback_off
        self.redprint = redprint
        self.blackprint = blackprint
        self.greenprint = greenprint
        self.yellowprint = yelllowprint
        self.blueprint = blueprint
        self.cyanprint = cyanprint
        self.whiteprint = whiteprint
        self.magentaprint = magentaprint


class FeedbackTimer(object):
    """Simple class to provide feedback to user, with time elapsed to run task."""

    def __init__(self, msg=None):
        if msg:
            self.start(msg)

    def done(self):
        elapsed = str(int(time.time() - self.start_time))
        print(f"DONE ({elapsed}s)", flush=True)

    def start(self, msg):
        self.start_time = time.time()
        print(msg, end="...\n", flush=True)

    def tick(self, msg):
        elapsed = str(int(time.time() - self.start_time))
        print(f"{msg} ({elapsed}s)", end="...\n", flush=True)

    def tock(self, msg):
        return self.tick(msg)


class ConsoleHistogram(object):
    """Renders a histogram of data to the console.

    Args:
        data (dict or list): dict if already compiled, list if raw
        data_type (str): organization of data. options: compiled, raw. default: raw
        graph_char (str): character to use in graph. default: #
        graph_width (int): maximum number of characters in histogram bar. default: 40
        sort (str): how to sort the output. options: key, value. default: key
        title (str): title of histogram. default: None.
        border (bool): whether to print a border around histogram. default: True
        order (str): how to sort the output. options: asc, desc, None. default: None
    """

    def __init__(
        self,
        data,
        data_type="raw",
        graph_char="#",
        graph_width=40,
        sort="key",
        title=None,
        border=True,
        order=None,
    ):
        self.title = title
        self.border = border
        self.data = data
        self.data_type = data_type
        self.sort = sort
        self.graph_char = graph_char
        self.graph_width = graph_width
        self.order = order
        self._compile_data()

    def _num_chars(self, x):
        self.max_x = max(val for val in self.graph_data.values())
        divisor = self.max_x / self.graph_width
        return int(math.floor(x / divisor))

    def _compile_data(self):
        if self.data_type == "raw":
            self.graph_data = Counter(self.data)
        elif self.data_type == "compiled":
            self.graph_data = self.data

        if self.sort == "key":
            sort_elem = 0
        else:
            sort_elem = 1

        if self.order == "asc":
            d = sorted(self.graph_data.items(), key=lambda x:x[sort_elem], reverse=False)
            self.graph_data = dict(d)
        elif self.order == "desc":
            d = sorted(self.graph_data.items(), key=lambda x:x[sort_elem], reverse=True)
            self.graph_data = dict(d)

    def render(self):
        if self.border:
            print("-" * 80)
        if self.title:
            print(self.title)
        for x, tally in self.graph_data.items():
            print(f"{x:<10} {tally:<6}", "#" * self._num_chars(tally))
        if self.border:
            print("-" * 80)


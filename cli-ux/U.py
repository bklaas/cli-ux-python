"""Generic cli UX methods and classes for a richer console-driven experience."""
#import glob
#from pathlib import Path

from tqdm import tqdm

#from .__about__ import VERSION, MAJOR_VERSION

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
        print(msg, end="...", flush=True)


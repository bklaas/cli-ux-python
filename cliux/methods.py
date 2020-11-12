"""Generic cli UX methods for a richer console-driven experience."""
# import glob
# from pathlib import Path

from tqdm import tqdm


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

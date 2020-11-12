"""Generic cli UX classes for a richer console-driven experience."""
import time


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
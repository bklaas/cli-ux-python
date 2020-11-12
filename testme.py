import cliux

import time

for x in cliux.pbar(range(10)):
    time.sleep(1)

t = cliux.FeedbackTimer(msg="Starting")
for x in range(10):
    time.sleep(1)
    t.tick("Nonsensical processing!")
t.done()

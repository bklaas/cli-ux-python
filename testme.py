import cliux

import time

test = {"foo": "bar"}
cliux.cprint("This is a red message", "yes it is", test, color="red")
cliux.redprint("This is a red message")
cliux.cprint("This is a yellow message", color="yellow")
cliux.yellowprint("This is a yellow message")

cli = cliux.CliUx()

cli.traceback_off()
raise AssertionError("This is an assertion error")

for x in cliux.pbar(range(2)):
    time.sleep(1)

t = cliux.FeedbackTimer(msg="Starting")
for x in range(2):
    time.sleep(1)
    t.tick("Nonsensical processing!")
t.done()

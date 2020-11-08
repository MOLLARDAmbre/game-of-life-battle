"""
This file provides a function to make sure the players are not taking too long to answser
"""

import signal

def handler(signum, frame):
    raise Exception("Taking too long")

def limit_time(f, t_max):
    signal.signal(signal.SIGVTALRM, handler)  # When a sigvtalrm is raised, handle it with the function handle
    signal.setitimer(signal.ITIMER_VIRTUAL, t_max)  # In t_max, send a sigvtalrm
    try:
        res = f()  # Try to run f
    except:
        res = None  # Took too long
    signal.setitimer(signal.ITIMER_VIRTUAL, 0)  # Removes the sigvtalrm supposed to be raised soon
    return res

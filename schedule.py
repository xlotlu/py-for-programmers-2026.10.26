#!/usr/bin/env python3


import sys
import datetime as dt


def parse_timespec(timespec):
    """
    Parses a timespec in the format
    "[H]H:MM:SS" or "[H]H:MM" or "[H]H"
    """
    return dt.time.fromisoformat(timespec)



def get_delta_from(when: dt.time):
    now = dt.datetime.now()

    then = dt.datetime.combine(now, when)
    if now > then:
        # this timpespec is tomorrow.
        then += dt.timedelta(days=1)

    delta = then - now

    return delta



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(color=True)

    parser.add_argument("--countdown", action="store_true", default=False,
                        help="Enable countdown mode"
    )

    parser.add_argument("timespec",
                        help="Required time specification"
    )

    parser.add_argument("payload", nargs="?", default=None,
                        help="Optional payload"
    )

    args = parser.parse_args()

    print(f"Countdown: {args.countdown}")
    print(f"Timespec:  {args.timespec}")
    print(f"Payload:   {args.payload}")


    delta = get_delta_from(
        parse_timespec(args.timespec)
    )

    print(f"will wait for: {delta}")

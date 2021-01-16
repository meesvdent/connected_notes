"""the editor"""

import sys


def get_user_input():
    print("type your input, close with enter than cntr+D\n")
    try:
        raw = sys.stdin.read()
        print("\n")
    except KeyboardInterrupt:
        print("not saved")

    return raw





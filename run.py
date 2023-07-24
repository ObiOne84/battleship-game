import time
import sys
from random import randint


def print_out(data):
    """
    The function will display text as it typed in real
    time rather than dispaly all message at once
    """
    for letter in data:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
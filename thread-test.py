#!/usr/bin/env python

from threading import Thread
from random import randint
import itertools
import sys
import timeit


class Worker:
    """
    Worker Class

    Initialize the Worker class for the multi-threaded computations
    """
    def __init__(self):

        # number of computations to perform
        self.computations = 100000

        # the number to start the computation at
        self.start_at = 6

    def do_math(self):
        """
        Do Math

        Compute the algorithm for stressing the CPU 
        :return: 
        """
        # initialize the timer to measure how long each process takes
        start = timeit.default_timer()

        # start the computation at a reasonable number
        # mostly to avoid multiplying by 0 or 1, which is not computationally intensive.
        result = self.start_at
        for _ in itertools.repeat(None, self.computations):
            result = (result * randint(1, 9)) / randint(1, 5)

        # stop the timer, print the results
        stop = timeit.default_timer()
        print result
        print("\nThread took {} seconds to run\n\n".format(stop - start))

if __name__ == "__main__":

    # Initialize the Server Object
    worker = Worker()

    # Call send(), handle errors and close socket if exception
    try:
        j1 = Thread(target=worker.do_math, args=())
        j2 = Thread(target=worker.do_math, args=())
        j3 = Thread(target=worker.do_math, args=())
        j4 = Thread(target=worker.do_math, args=())
        j5 = Thread(target=worker.do_math, args=())

        j1.start()
        j2.start()
        j3.start()
        j4.start()
        j5.start()

    except (KeyboardInterrupt, SystemExit) as e:
        sys.exit()

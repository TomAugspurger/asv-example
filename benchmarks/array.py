import time
import timeit


class Main(object):

    goal_time = 2.0
    timer = timeit.default_timer

    def setup(self):
        pass

    def time_it(self):
        time.sleep(1.5)

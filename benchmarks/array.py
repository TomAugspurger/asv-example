import time
import timeit


class Main(object):

    timer = timeit.default_timer

    def setup(self):
        pass

    def time_it(self):
        time.sleep(.001)

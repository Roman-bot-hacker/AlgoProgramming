from math import sqrt
import collections
import functools

class memoized(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


distance = 100
max_heights = [5,12,48,62,71,1,24,78,100,22,24]


def find_max_length(v_distance, v_max_heights):
    return round(max(__recursive_fun(len(max_heights) - 2, 0, 1)[0],
                     __recursive_fun(len(max_heights) - 2, 0, max_heights[-1])[0]), 2)


@memoized
def __recursive_fun(step, wires_len, previous_height):
    if step > 0:
        rec1 = __recursive_fun(step - 1, __get_length(distance, previous_height, 1) + wires_len, 1)
        rec2 = __recursive_fun(step - 1, __get_length(distance, previous_height, max_heights[step]) + wires_len, max_heights[step])
    if step == 0:
        rec1 = (__get_length(distance, previous_height, 1) + wires_len, 1)
        rec2 = (__get_length(distance, previous_height, max_heights[step]) + wires_len, max_heights[step])
    if rec1[0] > rec2[0]:
        wires_len = rec1[0]
        current_height = rec1[1]
    else:
        wires_len = rec2[0]
        current_height = rec1[1]
    return wires_len, current_height


def __get_length(distance, h1, h2):
    h = h2 - h1
    return sqrt(h ** 2 + distance ** 2)

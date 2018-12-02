from math import sqrt
import collections
import functools

def find_max_length(v_distance, v_max_heights):
    return round(max(__find_wires_length(len(max_heights) - 2, 0, 1)[0],
                     __find_wires_length(len(max_heights) - 2, 0, max_heights[-1])[0]), 2)

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


@memoized
def __find_wires_length(step, wires_len, previous_height):
    if step > 0:
        height_min = __find_wires_length(step - 1, __length_between_pillars(distance, previous_height, 1) + wires_len, 1)
        height_max = __find_wires_length(step - 1, __length_between_pillars(distance, previous_height, max_heights[step]) + wires_len, max_heights[step])
    if step == 0:
        height_min = (__length_between_pillars(distance, previous_height, 1) + wires_len, 1)
        height_max = (__length_between_pillars(distance, previous_height, max_heights[step]) + wires_len, max_heights[step])
    if height_min[0] > height_max[0]:
        wires_len = height_min[0]
        current_height = height_min[1]
    else:
        wires_len = height_max[0]
        current_height = height_min[1]
    return wires_len, current_height


def __length_between_pillars(distance, h1, h2):
    h = h2 - h1
    return sqrt(h ** 2 + distance ** 2)
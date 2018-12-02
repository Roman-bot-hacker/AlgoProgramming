from math import sqrt

def find_max_length(distance, max_heights):
    first_height_max = __find_max_length(distance, __find_heights_by_first_height(max_heights))
    max_heights[0] = 1
    first_height_min = __find_max_length(distance, __find_heights_by_first_height(max_heights))
    return max(first_height_max, first_height_min)


def __find_heights_by_first_height(heights):
    for i in range(1, len(heights)):
        if heights[i - 1] == 1:
            pass
        else:
            heights[i] = 1
    return heights


def __find_max_length(distance, heights):
    max_length = 0.0
    for i in range(1, len(heights)):
        max_length += sqrt(distance ** 2 + (heights[i] - heights[i - 1]) ** 2)
    return round(max_length, 2)

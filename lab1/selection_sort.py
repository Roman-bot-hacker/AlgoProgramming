from counter import Counter


# selection sort of printing speed from the fastest to the slowest
def Selection_sort(list):
    N = len(list)
    for i in range(0, N - 1):
        min_index = i
        for j in range(i + 1, N):
            if list[j].speed > list[min_index].speed:
                min_index = j
            Counter.compare_count()
        list = swap(list, i, min_index)
        Counter.exchange_count()
    return list


def swap(list, i, min_index):
    tmp = list[i]
    list[i] = list[min_index]
    list[min_index] = tmp
    return list
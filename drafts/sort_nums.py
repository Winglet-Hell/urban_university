def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


def selection_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]


def insertion_sort(ls):
    for i in range(1, len(ls)):
        current = ls[i]
        j = i - 1
        while j >= 0 and current < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = current

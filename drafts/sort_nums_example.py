import sort_nums as sn

# Три переменные со списками чисел от 1 до 10 в разном порядке
nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nums2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
nums3 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

# Сортировка списков
sn.bubble_sort(nums1)
sn.selection_sort(nums2)
sn.insertion_sort(nums3)

# Вывод отсортированных списков
print(nums1)
print(nums2)
print(nums3)

list1 = [10, 20, 30, 40, 5]
list2 = [30, 40, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
print(list(common))
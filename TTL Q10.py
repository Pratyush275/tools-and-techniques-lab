my_list = [1, 2, 3, 4, 5]
i = 2
j = 4

temp = my_list[i]
my_list[i] = my_list[j]
my_list[j] = temp

print(my_list)
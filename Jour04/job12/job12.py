def sort_list(list):
    n = 0
    while n < len(list) - 1:
        if list[n] > list[n + 1]:
            list[n], list[n + 1] = list[n + 1], list[n]
            n = 0
        else:
            n += 1
my_list = [5, 2, 9, 1, 5, 6]
sort_list(my_list)
print(my_list)

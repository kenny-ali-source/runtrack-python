def function():
    list=[8,24,48,2,16]
    count = 0
    for i in list:
        if i % 3 == 0:
            count += 1
    return count
print(function())
def function():
    L = [1, 2, 3, 4, 5]
    value = ' '.join(map(str, L))
    print(value)
    L[0], L[4] = L[4], L[0]
    value_1 = ' '.join(map(str, L))
    print(value_1)
function()

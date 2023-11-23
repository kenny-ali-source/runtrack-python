def function():
    L=[1,2,3,4,5]
    value =' '.join(str(L[0:5]))
    print(value)
    value_1 = ' '.join(str(L[1:2]))
    print(value_1)
    the_sum = L[2]+L[4]
    L[3] = the_sum
    value_2 = ' '.join(str(L[0:5]))
    print(value_2)
    value_3 = ' '.join(str(L[4]))
    print(value_3)
print(function())
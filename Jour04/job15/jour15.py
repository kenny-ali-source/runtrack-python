def function(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def function_2(list):
    for i in range(len(list)):
        list[i] = int(list[i] + 0.5)
    function(list)
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
function_2(L)
print(L)

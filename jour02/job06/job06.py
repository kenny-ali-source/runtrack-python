for n in range(2, 1001):
    prime_number = True
    for i in range(2, n):
        if n % i == 0:
            prime_number = False
            break
    if prime_number == True:
         print(n)
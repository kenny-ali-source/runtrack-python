for n in range(2, 1001):
    prime_numbers = True
    for i in range(2, n):
        if n % i == 0:
            prime_numbers = False
            break
    if prime_numbers == True:
         print(n, end=' ')
print("\n")
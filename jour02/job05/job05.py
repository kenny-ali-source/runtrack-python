resultat = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        resultat += i
        print("FizzBuzz", end=' ')
    elif i % 3 == 0:
        resultat += i
        print("Fizz", end=' ')
    elif i % 5 == 0:
        resultat += i
        print("Buzz", end=' ')
    else:
        print(i, end=' ')
print("\n")

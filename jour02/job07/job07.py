string = "abcdefghijklmnopqrstuvwxyz" * 10
for i in range(0, len(string)):
    for j in range(0, i):
        print(string[j], end=' ')
    print()



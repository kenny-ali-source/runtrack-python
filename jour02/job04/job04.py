n = int(input("Entrer un nombre supérieur à zéro (N):"))
message = print("la table de multiplication de :", n,":")
for i in range(1,11):
    if n ==0:
        quit()
    print(n,"x",i, "=",i*n)



n = int(input("Entrer un nombre supérieur à 0:"))
print("la table de multiplication de :", n," est :")
for i in range(1,11):
    if n ==0:
        quit()
    print(n,"x",i, "=",i*n)



def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "Le nombre est pair."
        else:
            return "Le nombre est impair."
    else:
        return "ce nombre n'est pas un entier positif."
print(verifie_pair_impair(10))
print(verifie_pair_impair(5))
print(verifie_pair_impair(3))
print(verifie_pair_impair(-5))
print(verifie_pair_impair(-3))

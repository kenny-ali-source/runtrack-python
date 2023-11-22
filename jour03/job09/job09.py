def moyenne(grade_1, grade_2, grade_3):
    return (grade_1 + grade_2 + grade_3) / 3

grade_1 = float(input("Entrez la première note : "))
grade_2 = float(input("Entrez la deuxième note : "))
grade_3 = float(input("Entrez la troisième note : "))
moyenne_etudiant = moyenne(grade_1, grade_2, grade_3)
print("La moyenne de l'étudiant est :", moyenne_etudiant, "par conséquent tu es un,")
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève.")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève.")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen.")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts.")
else:
    print("La moyenne n'est pas dans une plage valide.")


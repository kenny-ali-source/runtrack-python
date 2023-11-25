def my_long_word(longueur_minimale, phrase):
    mot_actuel = ''
    mots_plus_longs = ''
    for caractere in phrase:
        if caractere.isalnum() or caractere == "'":
            mot_actuel += caractere
        elif mot_actuel != '':
            if len(mot_actuel) > longueur_minimale:
                mots_plus_longs += mot_actuel + ' '
            mot_actuel = ''
    if len(mot_actuel) > longueur_minimale:
        mots_plus_longs += mot_actuel

    return mots_plus_longs
longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(longueur_minimale, phrase)
print("Output:", resultat)

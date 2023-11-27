def chiffrement_cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre.isalpha():
            est_majuscule = lettre.isupper()
            lettre = lettre.lower()
            lettre_codee = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))

            if est_majuscule:
                lettre_codee = lettre_codee.upper()
            resultat += lettre_codee
        else:
            resultat += lettre

    return resultat
message_original = "Bonjour, Jules César!"
decalage = 3
message_code = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_code)

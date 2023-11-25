montant_initial = 10000.0
taux_rendement_annuel = 5.0
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial:", gain_annuel, "euros")
montant_initial += 5000
taux_rendement_annuel += 2
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel après augmentation du capital et du taux de rendement:", nouveau_gain_annuel, "euros")
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1
montant_final = montant_initial + nouveau_gain_annuel
print("Montant final de l'investissement après retrait et diminution du rendement:", montant_final, "euros")

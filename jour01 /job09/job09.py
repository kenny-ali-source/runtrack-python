nom_produit = "Iphone"
prix_unitaire = 1000.0
quantite_en_stock = 50
print("Produit:", nom_produit)
print("Prix unitaire:", prix_unitaire, "€")
print("Quantité en stock:", quantite_en_stock)

quantite_acheter = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock += quantite_acheter
prix_unitaire *= 1.1
print("\nAprès l'achat de", quantite_acheter, "produit(s) et l'inflation de 10% :")
print("Produit:", nom_produit)
print("Nouveau prix unitaire:", prix_unitaire, "€")
print("Nouvelle quantité en stock:", quantite_en_stock)

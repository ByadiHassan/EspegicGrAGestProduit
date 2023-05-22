from produit import Produit
from magasin import Magasin
from os import system

mag=Magasin()
choix=0
while choix !=5:
    system("cls")
    choix=int(input("1. Ajouter\n2. Afficher\n3. Enregistrer\n4."
    + "Ouvrir\n5. Quitter\nTapez votre choix ? "))
    if choix==1:
        id=int(input("Tapez l'id du produit : "))
        design=input("Tapez la désignation du produit : ")
        prix=float(input("Tapez le prix du produit : "))
        p=Produit(id,design,prix)
        mag.ajouter(p)
        #mag.ajouter(Produit(int(input("Tapez l'id du produit")),
        # input("Tapez la désignation du produit"),
        # float(input("Tapez le prix du produit"))))
    elif choix==2:
        mag.afficher()
        system("pause")
    elif choix==3:
        mag.enregistrer()
    elif choix==4:
        mag.charger()
        mag.afficher()
        system("pause")

    
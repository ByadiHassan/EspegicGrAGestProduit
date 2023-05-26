from produit import Produit
from magasin import Magasin
from clavier import Clavier
from os import system

mag=Magasin()
choix=0
while choix !=5:
    system("cls")
    
    choix=Clavier.getValue("1. Ajouter\n2. Afficher\n3. Enregistrer\n4."
    + "Ouvrir\n5. Quitter\nTapez votre choix ? ",int)
    
    if choix==1:       
        mag.ajouter(Clavier.getProduit())
       
    elif choix==2:
        mag.afficher()
        system("pause")
    elif choix==3:
        mag.enregistrer()
    elif choix==4:
        mag.charger()
        mag.afficher()
        system("pause")

    
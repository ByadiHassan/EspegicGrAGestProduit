from produit import Produit
from magasin import Magasin
from clavier import Clavier
from os import system

mag=Magasin()
choix=0
while choix !=6:
    system("cls")
    
    choix=Clavier.getInt("1. Ajouter\n2. Afficher\n3. Enregistrer\n4. "
    + "Ouvrir\n5. Chercher\n6. Quitter\nTapez votre choix ? ")
    
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
    elif choix==5:
        id =Clavier.getInt("Tapez l'id du produit à chercher ? ")
        if mag.exists(id):
            mag.chercher(id).afficher()
        else:
            print("Aucun produit ne possède cet id ! ")
        system("pause")

    
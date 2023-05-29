from produit import Produit
from magasin import Magasin
from clavier import Clavier
from habit import Habit
from os import system

mag=Magasin()
choix=0
while choix !=8:
    system("cls")
    
    choix=Clavier.getInt("1. Ajouter\n2. Afficher\n3. Enregistrer\n4. "
    + "Ouvrir\n5. Chercher\n6. Supprimer\n7. Ajouter Habit\n 8. Quitter\nTapez votre choix ? ")
    
    if choix==1:
        try:
            mag.ajouter(Clavier.getProduit())
        except Exception as ex:
            print(ex)
            system("pause")
       
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
    elif choix==6:
        id =Clavier.getInt("Tapez l'id du produit à supprimer ? ")
        if mag.exists(id):
            pr:Produit=mag.chercher(id)
            pr.afficher()
            rep=Clavier.getString("Etes vous sûr de vouloir supprimer ce produit O/N? ")
            if rep=='o' or rep=='O':
                mag.supprimer(pr)

        else:
            print("Aucun produit ne possède cet id ! ")
        system("pause")
    elif choix==7:
        try:
            mag.ajouter(Clavier.getHabit())
        except Exception as ex:
            print(ex)
            system("pause")    
        

    
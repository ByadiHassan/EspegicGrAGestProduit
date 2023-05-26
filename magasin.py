from produit import Produit
import pickle
class Magasin:
    def __init__(self):
        self.__produits=list()

    def getProduits(self)    :
        return self.__produits
    def setProduits(self,produits):
        self.__produits=produits

    def ajouter(self,produit:Produit):
        self.__produits.append(produit)

    def supprimer(self,produit:Produit):
        self.__produits.remove(produit)
    def afficher(self):
        for produit  in self.__produits:
            produit.afficher()
    def enregistrer(self):
        fichier=open("produit.bin","wb")
        pickle.dump(self.__produits,fichier)
        fichier.close()

    def charger(self):
        fichier=open("produit.bin","rb")
        self.__produits=pickle.load(fichier)
        fichier.close()

    def exists(self,id):
        existance =False
        for pr in self.__produits:
            if pr.getId()==id:
                existance =True
                break
        return existance            

    def chercher(self,id):
        for pr in self.__produits:
            if pr.getId()==id:
                return pr
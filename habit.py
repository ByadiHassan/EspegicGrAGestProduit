from produit import Produit
class Habit(Produit):
    def __init__(self,id,design,prix,couleur,taille):
        super().__init__(id,design,prix)
        self.setCouleur(couleur)
        self.setTaille(taille)

    def getCouleur(self):
        return self.__couleur
    def setCouleur(self,couleur):
        if len(couleur)>0:
            self.__couleur=couleur
        else:
            ex=Exception("Attention la couleur  du produit ne doit pas être vide !")
            raise ex
    def getTailler(self):
        return self.__taille

    def setTaille(self,taille):
        if len(taille)>0:
            self.__taille=taille
        else:
            ex=Exception("Attention la taille  du produit ne doit pas être vide !")
            raise ex
    def __str__(self):
        return super().__str__()+ '\t'+ self.__couleur+ '\t'+self.__taille
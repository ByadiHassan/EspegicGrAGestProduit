from os import system
from habit import Habit
from produit import Produit
class Clavier:
    @staticmethod
    def getString(msg):
        return input(msg)
    
    @staticmethod
    def getInt(msg):
        while True:
            try:
                return int(Clavier.getString(msg))               

            except Exception as ex:
                print(ex)
                system('pause')
                system('cls')

    @staticmethod
    def getFloat(msg):
        while True:
            try:
                return float(Clavier.getString(msg))               

            except Exception as ex:
                print(ex)
                system('pause')
                system('cls')
    @staticmethod
    def getValue(msg,f):
        while True:
            try:
                return f(Clavier.getString(msg))            
            except Exception as ex:
                print(ex)
                system('pause')
                system('cls')

    @staticmethod
    def getProduit():
        return Produit(Clavier.getInt("Tapez l'id du produit : "),
        Clavier.getString("Tapez la désignation du produit : "),
        Clavier.getFloat("Tapez le prix du produit : "))
    @staticmethod
    def getHabit():
        return Habit(Clavier.getInt("Tapez l'id du produit : "),
        Clavier.getString("Tapez la désignation du produit : "),
        Clavier.getFloat("Tapez le prix du produit : "),
        Clavier.getString("Tapez la couleur du produit : "),
        Clavier.getString("Tapez la taille du produit : "))

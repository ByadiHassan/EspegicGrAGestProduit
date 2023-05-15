from produit import Produit

try:
    p=Produit(10,'Ecran',250)
    p.afficher()
except Exception as ex:
    print(ex)



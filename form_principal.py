import tkinter as tk
from form_gestion_produit import FormGestionProduit
from form_gestion_habit import FormGestionHabit
from form_gestion_produit_electrique import FormGestionProduitElectrique

class FormPrincipal:
    def __init__(self) :
        self.root=tk.Tk()
        self.root.geometry("820x500")
        self.root.title("Formulaire principal")
        self.root.iconbitmap('free.ico')
        self.lblBienvenu=tk.Label(self.root,bd=10,relief="sunken",padx=20,pady=10,
        text="Bienvenu dans l'application Gestion des produits",bg="blue",fg="white",
        font="Arial 16 bold italic")
        self.lblBienvenu.pack(side="top")

        self.btnQuitter=tk.Button(self.root,bd=10,relief="groove",
        command=self.quitter,padx=20,pady=10,text="Quitter",bg="red",fg="white",
        font="Arial 16 bold italic")
        self.btnQuitter.pack(side=tk.BOTTOM)

        self.frameButton=tk.Frame(self.root,bg='yellow',padx=20,pady=20)
        self.frameButton.pack(expand=1)

        self.btnGestionProduit=tk.Button(self.frameButton,bd=10,relief="groove",
        command=self.openFormGestioProduit,text="Gestion des Produits",bg="blue",fg="white",
        font="Arial 16 bold italic")
        self.btnGestionProduit.pack(side="left")

        self.btnGestionHabit=tk.Button(self.frameButton,bd=10,relief="groove",
        command=self.openFormGestioHabit,text="Gestion des Habits",bg="blue",fg="white",
        font="Arial 16 bold italic")
        self.btnGestionHabit.pack(side="left")

        self.btnGestionProduitElec=tk.Button(self.frameButton,bd=10,relief="groove",
        command=self.openFormGestioProduitElectrique,text="Gestion des Produits Elec.",bg="blue",fg="white",
        font="Arial 16 bold italic")
        self.btnGestionProduitElec.pack(side="left")





        self.root.mainloop()
        
    def quitter(self):
        self.root.destroy()

    def openFormGestioProduit(self):
        FormGestionProduit(self.root)

    def openFormGestioHabit(self):
        FormGestionHabit()
        
    def openFormGestioProduitElectrique(self):
        FormGestionProduitElectrique()

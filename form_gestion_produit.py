import tkinter as tk
class FormGestionProduit:
    def __init__(self,fenetre:tk.Tk) -> None:

        self.fenetre=fenetre
        self.fenetre.iconify()
        self.root=tk.Tk()
        self.root.geometry("800x600")
        self.btnFermer=tk.Button(self.root,bd=10,relief="groove",
        command=self.fermer,padx=20,pady=10,text="Fermer",bg="orange",fg="white",
        font="Arial 16 bold italic")
        self.btnFermer.pack(side=tk.BOTTOM)

        self.root.mainloop()
    def fermer(self):
        self.fenetre.deiconify()
        self.root.destroy()
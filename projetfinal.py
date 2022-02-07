
from cProfile import label
from email import message
import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter as tk
import json


def ajouter():

    liste = []
    data = {
        "Nom" : entrernom.get(),
        "Prenom" : entrerprenom.get(),
        "Age" : entrerage.get(),
        "Adresse" : entreradresse.get(),
        "Telephone" : entrerTelephone.get(),
        "chambre" : listeCombo.get(),
        "docteur" : docliste.get(),
        "genre" : genre.get(),
         }
    liste.append(data)
    try:
        with open("projet.json", "r") as f:
            json.load(f)
    
    except json.decoder.JSONDecodeError:

        with open ("projet.json", "w") as f:
            json.dump(liste, f , indent=4)
        
    else: 
        with open("projet.json", "r") as f:
            nixon=json.load(f)
            nixon.append(data)
    
        with open ("projet.json", "w") as f:
            json.dump(nixon, f , indent=4)
        
        if (entrernom==""or entrerprenom=="" or entrerage=="" or entreradresse=="" or entrerTelephone =="" ):
            messagebox.showerror("error","Veuillez remplir les differents champs")
     
    

        
    entrernom.delete(0, END)
    entrerprenom.delete(0, END)
    entrerage.delete(0, END)
    entreradresse.delete(0, END)
    entrerTelephone.delete(0, END)
    listeCombo.set('')
    docliste.set('')
    genre.set('')




    # Nom = entrernom.get()
    # Prenom = entrerprenom.get()
    # Age = entrerage.get()
    # Adresse = entreradresse.get()
    # Telephone = entrerTelephone.get() 


   

def quitter ():
    Nom = entrernom.get()
    Prenom = entrerprenom.get()
    Age = entrerage.get()
    Adresse = entreradresse.get()
    Telephone = entrerTelephone.get()
    
    

def supprimer ():
    Nom = entrernom.get()
    Prenom = entrerprenom.get()
    Age = entrerage.get()
    Adresse = entreradresse.get()
    Telephone = entrerTelephone.get()


projet = Tk()
projet.title("GESTION DES HOSPITALISATIONS",)
projet.geometry("1300x700")

titre = Label(projet,bd = 20, relief = RIDGE, text ="GESTION DES HOSPITALISATIONS", font = ("Arial",30), bg = "GREEN", fg = "black")
titre.place(x =0, y = 0, width = 1365)

enregistrement = Label(projet,bd = 10, relief = GROOVE, text = "VEUILLEZ ENREGISTREMENT LE PATIENT SVP", font = ("italic"), fg = "black")
enregistrement.place(x =150, y =80, width=1000)

Nom = Label(projet, text= "NOM DU PATIENT", fg="green", bg="yellow", font=("italic", 16))
Nom.place(x=0, y=200, width=200)
entrernom = Entry(projet)
entrernom.place(x=200,y=197,width=300,height=30)


Prenom = Label(projet, text= "PRENOM DU PATIENT", fg="green", bg="yellow", font=("italic", 16))
Prenom.place(x=0, y=250, width=200)
entrerprenom = Entry(projet)
entrerprenom.place(x=200,y=247,width=300,height=30)

age = Label(projet, text= "AGE DU PATIENT", fg="green", bg="yellow", font=("italic", 16))
age.place(x=0, y=300, width=200)
entrerage = Entry(projet)
entrerage.place(x=200,y=297,width=300,height=30)

adresse = Label(projet, text= "ADRESSE DU PATIENT", fg="green", bg="yellow", font=("italic", 16))
adresse.place(x=0, y=350, width=200)
entreradresse = Entry(projet)
entreradresse.place(x=200,y=347,width=300,height=30)


Telephone = Label(projet, text= "TELEPHONE DU PATIENT", fg="green", bg="yellow", font=("italic", 16))
Telephone.place(x=0, y=400, width=200)
entrerTelephone = Entry(projet)
entrerTelephone.place(x=200,y=397,width=300,height=30)


docteur = Label(projet, text = "NOM DU DOCTEUR", fg= "green", bg= "yellow", font =("italic", 16))
docteur.place(x=0, y=450, width=200)
combodocteur=["Mr YAO", "Mr KOFFI", "Mr YLY", "Mr BROU"]
docliste = ttk.Combobox(projet, values=combodocteur)
docliste.set('')
docliste.place(x =200, y =449, width=200)


chambre = Label(projet, text = "NUMERO DE CHAMBRE", fg= "green", bg= "yellow", font =("italic", 16))
chambre.place(x=0, y=500, width=200)
listechambre=["CHAMBRE 1", "CHAMBRE 2", "CHAMBRE 3", "CHAMBRE 4"]
listeCombo = ttk.Combobox(projet, values=listechambre)
listeCombo.set('')
listeCombo.place(x =200, y =499, width=200)

genre = Label(projet, text= "GENRE", font =("arial",16), bg ="yellow", fg="green")
genre.place(x=0, y=550, width=200)
listegenre=["Masculin", "FEMININ"]
genre = ttk.Combobox(projet, values=listegenre)
genre.set('')
genre.place(x =200, y =549, width=200)


#Radiobutton(projet, text="HOMME",padx= 5, value=1).place(x=650, y=500)

#Radiobutton(projet, text="FEMME",padx= 5, value=2).place(x=550, y=500)

btnenregistrer =Button(projet, text= "Enregistrer", font=("Arial", 16),bg = "green", fg = "red", command = ajouter)
btnenregistrer.place(x=40,y=600,width=200,height=30)

btnmodifier =Button(projet, text= "quitter", font=("Arial", 16),bg = "green", fg = "red", command = projet.destroy)
btnmodifier.place(x=250,y=600,width=200,height=30)


btnsupprimer =Button(projet, text= "Supprimer", font=("Arial", 16),bg = "green", fg = "red", command = supprimer)
btnsupprimer.place(x=150,y=650,width=200,height=30)



#-----LISTE DES PATIENTS---------
patient = Label(projet, text = "LISTES DES PATIENTS", font = ("arial", 16), bg ="red", fg ="black")
patient.place(x=600, y=140, width=650)

tree = ttk.Treeview(projet, columns = (1,2,3,4,5,6,7,8), height=6, show = "headings")
tree.place(x=600, y=200 , width=700, height=350)

tree.heading(1 , text="Nom")
tree.heading(2, text = "Prenom")
tree.heading(3, text = "Age")
tree.heading(4, text = "adresse")
tree.heading(5, text = "Telephone")
tree.heading(6, text = "Nom du Docteur")
tree.heading(7, text = "Numero de chambre")
tree.heading(8, text = "Genre")

tree.column(1 , width=50)
tree.column(2 , width=100)
tree.column(3 , width=100)
tree.column(4 , width=100)
tree.column(5 , width=100)
tree.column(6 , width=100)
tree.column(7 , width=120)
tree.column(8 , width=40)















projet.mainloop()
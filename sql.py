
import cmd
import email
from email import message
from tkinter import*
import sqlite3
import tkinter
from tkinter import messagebox 
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def connexion ():
   conn = sqlite3.connect("/Users/imac_10/Desktop/evaluation-1/mynixon.db")
   nom = entrernom.get()
   prenom =  entrerprenom.get()
   email =  entrermail.get()
   motdepasse = entrerMOTDEPASSE.get()
   confirm  =  entrercmdp.get()
   data_user = {
         'nom': nom,
         'prenom': prenom,
         'email': email,
         'motdepasse' : motdepasse
        
       }
   if(re.search(regex,entrermail.get())) :
      messagebox.showinfo("zoooo","votre email est  valide")
     
   else:
      messagebox.showerror("error","veuillez remplir tous les champs!")
   
   if(re.search(regex,entrermail.get())) :
      messagebox.showinfo("zoooo","votre email est  valide")
      
      
      c = conn.cursor()
   
      #data_user = {
            #'Nom': entrernom.get(),
            #'Prenom': entrerprenom.get(),
            #'mail': entrermail.get(),
            #'motdepasse' : entrerMOTDEPASSE.get(),
            #'cmdp': entrercmdp.get()
         #}
      c.execute("""CREATE TABLE IF NOT EXISTS user(
            nom text, 
            prenom text,
            email text,
            motdepasse text
         

         )""")
      
      c.execute("INSERT INTO user VALUES(:nom, :prenom, :email, :motdepasse  )", data_user)

      


      conn.commit()
      conn.close()

   else:
      messagebox.showerror("error",  "VOTRE EMAIL EST invalide")

   entrernom.delete(0, END)
   entrerprenom.delete(0, END)
   entrermail.delete(0, END)
   entrerMOTDEPASSE.delete(0, END)
   entrercmdp.delete(0, END)

sql = Tk()
sql.title("formulaire d'inscription")
sql.geometry("700x450")


Nom = Label(sql, text= "NOM", fg="green", bg="pink", font=("italic", 16))
Nom.place(x=0, y=50, width=200)
entrernom = Entry(sql)
entrernom.place(x=200,y=47,width=300,height=30)


Prenom = Label(sql, text= "PRENOM", fg="green", bg="pink", font=("italic", 16))
Prenom.place(x=0, y=100, width=200)
entrerprenom = Entry(sql)
entrerprenom.place(x=200,y=97,width=300,height=30)

mail = Label(sql, text= "EMAIL", fg="green", bg="pink", font=("italic", 16))
mail.place(x=0, y=150, width=200)
entrermail = Entry(sql)
entrermail.place(x=200,y=147,width=300,height=30)

Motdepasse = Label(sql, text= "MOTDEPASSE", fg="green", bg="pink", font=("italic", 16))
Motdepasse.place(x=0, y=200, width=200)
entrerMOTDEPASSE = Entry(sql)
entrerMOTDEPASSE.place(x=200,y=197,width=300,height=30)


cmdp = Label(sql, text= "CONFIRMATION DU MDP", fg="green", bg="pink", font=("italic", 16))
cmdp.place(x=0, y=250, width=200)
entrercmdp = Entry(sql)
entrercmdp.place(x=200,y=247,width=300,height=30)

btnconnection =Button(sql, text= "Connexion", font=("Arial", 16),bg = "green", fg = "red", command=connexion)
btnconnection.place(x=250,y=347,width=200,height=30)



sql.mainloop()


###-creation de la BD---###








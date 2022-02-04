from syslog import LOG_INFO
from tkinter import*
from tkinter import messagebox
from turtle import width
import os
#def LOGIN():
    #username=entry1.get()
    #password=entry2.get()

   
def run():
   os.system('python3 "/Users/imac_10/Desktop/evaluation-1/PSANTE/projetfinal.py"')
def LOGIN():
   

    username=entry1.get()
    password=entry2.get()
    if (username=="" and password==""):
        messagebox.showinfo("","Veuillez remplir les differents champs")
    elif(username=="NIXON" and password=="NAN2021"):
        messagebox.showinfo("","Vous etes connecté ")
        run()
    else:
        messagebox.showinfo("","Identifiant et mot de passse incorrect")
    

accueil=Tk()
accueil.title("PAGE DE CONNEXION")
accueil.geometry("700x500")
accueil.configure(bg="#FF5733")
tv = StringVar
titre = Label(accueil,bd = 20, relief = RIDGE, text ="PAGE DE CONNEXION", font = ("Arial",30), bg = "#FFBD33", fg = "black")
titre.place(x =0, y = 0, width = 700)

#global entry1
#global entry2

Label(accueil,text="IDENTIFIANT").place(x=20,y=130, width="96", height=30)
Label(accueil,text="MOT DE PASSE").place(x=20,y=172, width="96", height=30)

entry1=Entry(accueil,bd=5)
entry1.place(x=140,y=130)

entry2=Entry(accueil,bd=5)
entry2.place(x=140,y=170)

Button(accueil,text="LOGIN", command=LOGIN,height=2,width=15, bd=4).place(x=100,y=230)






accueil.mainloop()






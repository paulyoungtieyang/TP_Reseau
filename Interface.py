
from Tkinter import*
class fenetre:
    
    def __init__(self):
        
        self.fen=Tk()
        self.fen.geometry("800x800")
        self.fen.wm_title("Interface restaurant")
        self.see = True


        #separation de la fenetre en panneaux 
        panneauTot = PanedWindow(self.fen,orient=HORIZONTAL,height=750,width=1000)
        pDroite = PanedWindow(self.fen,orient=VERTICAL,height=750,width=400,bg='pink')
        pGauche = PanedWindow(self.fen,orient=VERTICAL,height=750,width=500,bg='white')
        labelpDroite = Label(pDroite,text="Commandes",height=2,width=55,bg='#CAAD73')
        labelpDroite.pack()
        
        
        pGauche1 = PanedWindow(pGauche,orient=VERTICAL,height=400,width=500,bg='#F3DEB6')
        pGauche2 = PanedWindow(pGauche,orient=VERTICAL,height=350,width=500,bg='#F3DEB6')

        pGauche1.pack()
        pGauche2.pack()
        
        labelpGauche1 = Label(self.fen,text="Livreurs",height= 2,bg='#CAAD73')
        pGauche1.add(labelpGauche1)
        

        labelpGauche2 = Label(self.fen,text="Chiffre d'affaire",height = 2,bg='#CAAD73')
        pGauche2.add(labelpGauche2)
        bouton2 = Button(self.fen, text="Bouton provisoire 2", command=self.testBouton, height=3)
        pGauche2.add(bouton2)

        #Ajout des livreurs a droite de l'interface (3 sous forme de checkButton et 2 sous forme de label a nous de choisir ce qui est mieux)
        self.var_livreur1= IntVar()
        self.var_livreur1.set(0)
        self.livreur1 = Checkbutton(self.fen,bg='white', text="Livreur 1",command =self.actionCheckbutton1, variable=self.var_livreur1, height=4)

        
        self.var_livreur2= IntVar()
        self.var_livreur2.set(0)
        self.livreur2 = Checkbutton(self.fen,bg='white', text="Livreur 2",command =self.actionCheckbutton2, variable=self.var_livreur2, height=4)

        self.var_livreur3= IntVar()
        self.var_livreur3.set(0)
        self.livreur3 = Checkbutton(self.fen,bg='white', text="Livreur 3",command =self.actionCheckbutton3, variable=self.var_livreur3, height=4)

        self.livreur4 = Label(self.fen,text="Livreur 4",height = 4,bg='white')
        self.livreur5 = Label(self.fen,text="Livreur 5",height = 3,bg='white')
    
        pGauche1.add(self.livreur1)
        pGauche1.add(self.livreur2)
        pGauche1.add(self.livreur3)
        pGauche1.add(self.livreur4)
        pGauche1.add(self.livreur5)
        
        #Ajout de la liste client a gauche : a relier a la partie reseau (utiliser la liste de client reseau pour remplir la liste)
        list = Listbox(pDroite)
        sbar = Scrollbar(pDroite)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        for i in range(10):
            list.insert(i, "Client-" + str(i))
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        print (list)

        
        #pDroite.add(labelpDroite)
        panneauTot.add(pDroite)
        panneauTot.add(pGauche)

        panneauTot.pack()
        self.fen.mainloop()
        
    def testBouton(self):
        print ("coucou")


#Changement d'etat quand on clique sur les checkButton
    def actionCheckbutton1(self):
        if self.var_livreur1.get() == 1:
            self.livreur1.configure(bg='red')
        else :
            self.livreur1.configure(bg='white')

    def actionCheckbutton2(self):
        if self.var_livreur2.get() == 1:
            self.livreur2.configure(bg='red')
        else :
            self.livreur2.configure(bg='white')

    def actionCheckbutton3(self):
        if self.var_livreur3.get() == 1:
            self.livreur3.configure(bg='red')
        else :
            self.livreur3.configure(bg='white')
            
"""
    def actionCheckbutton4(self):
        if self.var_livreur4.get() == 1:
            self.livreur4.configure(bg='red')
        else :
            self.livreur4.configure(bg='white')
            
    def actionCheckbutton5(self):
        if self.var_livreur5.get() == 1:
            self.livreur5.configure(bg='red')
        else :
            self.livreur5.configure(bg='white')

    def run(self):
        if self.var_livreur1.get() == 1:
            self.livreur1.configure(bg='red')
            
        if self.var_livreur2.get() == 1:
            self.livreur2.configure(bg='red')
        
        if self.var_livreur3.get() == 1:
            self.livreur3.configure(bg='red')

        if self.var_livreur4.get() == 1:
            self.livreur4.configure(bg='red')

        if self.var_livreur5.get() == 1:
            self.livreur5.configure(bg='red')


    # pour se souvenir de comment faire un bouton
        bouton1 = Button(self.fen, text="Bouton panneau1", command=self.testBouton, height=3)
        bouton2 = Button(self.fen, text="Bouton panneau2", command=self.testBouton, height=3)
"""




fen = fenetre()

#fen.run()

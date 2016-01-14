
from Tkinter import*
class fenetre:
    
    def __init__(self):
        
        self.fen=Tk()
        self.fen.geometry("800x800")
        self.fen.wm_title("Interface restaurant")
        self.see = True


        #separation de la fenetre en panneaux 
        panneauTot = PanedWindow(self.fen,orient=HORIZONTAL,height=750,width=1000)
        pGauche = PanedWindow(self.fen,orient=VERTICAL,height=750,width=500,bg='white')
        self.pDroite = PanedWindow(self.fen,orient=VERTICAL,height=750,width=400,bg='white')
        
        labelpDroite = Label(self.pDroite,text="Commandes",height=2,width=55,bg='#CAAD73')
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
        
        self.var_livreur1= StringVar()
        self.livreur1 = Label(self.fen,textvariable=self.var_livreur1,height = 3,bg='white')
        self.var_livreur1.set("Livreur 1")
        
        self.var_livreur2= StringVar()
        self.livreur2 = Label(self.fen,textvariable=self.var_livreur2,height = 3,bg='white')
        self.var_livreur2.set("Livreur 2")
        
        self.var_livreur3= StringVar()
        self.livreur3 = Label(self.fen,textvariable=self.var_livreur3,height = 3,bg='white')
        self.var_livreur3.set("Livreur 3")
        
        self.var_livreur4= StringVar()
        self.livreur4 = Label(self.fen,textvariable=self.var_livreur4,height = 4,bg='white')
        self.var_livreur4.set("Livreur 4")
        
        self.var_livreur5= StringVar()
        self.livreur5 = Label(self.fen,textvariable=self.var_livreur5,height = 3,bg='white')
        self.var_livreur5.set("Livreur 5")
        self.listeLivreurVar = [self.var_livreur1,self.var_livreur2,self.var_livreur3,self.var_livreur4 ,self.var_livreur5]
        self.listeLivreur = [self.livreur1,self.livreur2,self.livreur3,self.livreur4 ,self.livreur5]
        
        pGauche1.add(self.livreur1)
        pGauche1.add(self.livreur2)
        pGauche1.add(self.livreur3)
        pGauche1.add(self.livreur4)
        pGauche1.add(self.livreur5)
        
        #Ajout de la liste client a gauche : a relier a la partie reseau (utiliser la liste de client reseau pour remplir la liste)
        #self.liste = Listbox(pDroite)
        sbar = Scrollbar(self.pDroite)
        #sbar.config(command=self.liste.yview)
        #self.liste.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        #for i in range(10):
        #    self.liste.insert(i, "Client-" + str(i))
        #self.liste.pack(side=LEFT, expand=YES, fill=BOTH)
        

        

        panneauTot.add(pGauche)
        panneauTot.add(self.pDroite)
        

        panneauTot.pack()
        #self.fen.mainloop()
        self.fen.update_idletasks()
        self.fen.update()
        
        
    def ajoutClient(self,num,statut):
		label = Label(self.pDroite, text="Client "+str(num)+": "+statut, bg="pink")
		label.pack()		
		self.fen.update_idletasks()
		self.fen.update()
		
    def testBouton(self):
        print ("coucou")


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
       
    def actionLivreur(self,livreur):
		print "je vais dans la methode action livreur"
		for i in xrange(len(self.listeLivreurVar)):
			#print livreur.nom, self.listeLivreurVar[i]
			#if self.listeLivreur[i]==slivreur:
				#self.listeLivreur[i].configure(bg="red")
				
			if self.listeLivreurVar[i].get()==livreur.nom and livreur.occupe==True:
				self.listeLivreur[i].configure(bg="red")
			if self.listeLivreurVar[i].get()==livreur.nom and livreur.occupe==False :
				 self.listeLivreur[i].configure(bg="green")		
		self.fen.update_idletasks()
		self.fen.update()

	
	

		     
"""
#comment faire un checkbox
self.var_livreur1= IntVar()
self.var_livreur1.set(0)
self.livreur1 = Checkbutton(self.fen,bg='white', text="Livreur 1",command =self.actionCheckbutton1, variable=self.var_livreur1, height=4)

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



#pour tester la fenetre seule

#f= fenetre()
#f.fen.update_idletasks()
#f.fen.update()

#fen.run()

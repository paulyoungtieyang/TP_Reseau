import socket 
import select
import time
import sys
import signal
import random


stopLoop = True
sLoop = True

class livreur:
	
	def __init__(self,num):
		self.num=num #Chaque livreur a un numero
		self.occupe=False #Un livreur peut etre occupe ou non par une livraison

	def __repr__(self):
		if self.occupe==False:
			return "Livreur"+str(self.num)+" : disponible\n"
		else :
			return "Livreur"+str(self.num)+" : occupe\n"
		

if len(sys.argv)<3:
        print "Vous devez donner le numero du livreur"
        sys.exit(-1)		
        
num=sys.argv[2] #Il faut donner un numero au client au moment de sa connexion au serveur
typ=sys.argv[1]
livreur1=livreur(num)		
t=0


try:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("",8001))

	
	while stopLoop:
	  	msg ="livreur "+str(livreur1.num)+" en attente pour une commande"
	  	s.send(msg)

		data = s.recv(255)
			
		t+=1
		if data=="Fin":
			print "La livraison est finie"
			break
				
			
			
  		


except socket.error, e:
    	print "erreur dans l'appel a une methode de la classe socket: %s" % e
    	sys.exit(1)
finally:
	s.shutdown(1)
	s.close()
	print "Fin du service"
	
	


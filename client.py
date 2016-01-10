import socket 
import select
import time
import sys
import signal
import random


stopLoop = True

class client:
	
	def __init__(self,d,num):
		self.distance=d #Distance entre le client et le restaurant pour calculer le temps qu'il faudra pour qu'il soit livre
		self.num=num #Chaque client a un numero
	def commande(self):
		n=random.randint(0,10) #On pourrait faire par exemple 10 menus differents
		commande = "Menu"+str(n)
		return commande
		

if len(sys.argv)<2:
        print "Vous devez donner un numero au client"
        sys.exit(-1)		
        
num=sys.argv[2] #Il faut donner un numero au client au moment de sa connexion au serveur
typ=sys.argv[1]
client1=client(10,num)		
t=0
c=client1.commande()

try:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("",8001))

	while stopLoop:
  		msg ="client"+str(client1.num)+" en attente pour un "+c
  		s.send(msg)
 

		data = s.recv(255)
		
		t+=1
  		#if t>client1.distance*20000 : break
  		if data=="Livraison":
  			break


except socket.error, e:
    	print "erreur dans l'appel a une methode de la classe socket: %s" % e
    	sys.exit(1)
finally:
	s.shutdown(0)
	s.close()
print "Le client a recu sa commande"


import socket
import threading
import time
import sys
import Interface





#############################################################################
#								CLASSE LIVREUR								#
#############################################################################

class livreur:
	
	def __init__(self,num):
		self.num=num #Chaque livreur a un numero
		self.occupe=False #Un livreur peut etre occupe ou non par une livraison

	def __repr__(self):
		if self.occupe==False:
			return "Livreur"+str(self.num)+" : disponible\n"
		else :
			return "Livreur"+str(self.num)+" : occupe\n"


restaurant = []
for i in xrange(5):
	restaurant.append(livreur(i+1))


restaurant[0].occupe=True #Pour tester si ca marche de prendre le 1er livreur dispo



#############################################################################
#								PARTIE SERVEUR								#
#############################################################################
listeClient=[]

def f_thread(clisock):
    loopEnd = True
    t=0
    time=0
    #On cherche le premier livreur disponible:
    num_livreur=0 
    while restaurant[num_livreur].occupe==True:
		num_livreur +=1
		
    restaurant[num_livreur].occupe=True  
  
    while loopEnd:
		data = clisock.recv(2048)
		if t==0:
			print data
			print "ok3"
			num = data[6]
			num=len(listeClient)
			f.ajoutClient(num, "en attente")
		clisock.send(data)
		t+=1
		
		if not data or time>50000:
			clisock.send("end")
			clisock.shutdown(0)
			listeClient.remove(clisock)
			print "Le client"+str(num)+" a ete livre par le livreur"+str(restaurant[num_livreur].num)
			restaurant[num_livreur].occupe=False
			loopEnd = False
		time+=1
		print time
	
def f_thread_GUI():
	global f
	f=Interface.fenetre()

		
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',8001))
sock.listen(5)

while True:
	t1=threading.Thread(target=f_thread_GUI)
	t1.start()
	clisock, addr = sock.accept()
	listeClient.append(clisock)
	print "Un client a passe commande"
	t = threading.Thread(target=f_thread, args=(clisock,))
	t.start()


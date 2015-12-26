
import socket
import threading
import time
import sys



class livreur:
	
	def __init__(self,num):
		self.num=num #Chaque livreur a un numero
		self.occupe=False #Un livreur peut etre occupe ou non par une livraison

	def __repr__(self):
		if self.occupe==False:
			return "Livreur"+str(self.num)+" : disponible"
		else :
			return "Livreur"+str(self.num)+" : occupe"


restaurant = []
for i in xrange(1):
	restaurant.append(livreur(i))





#############################################################################
#								PARTIE SERVEUR								#
#############################################################################
listeClient=[]

def f_thread(clisock):
    loopEnd = True
    t=0
  
    while loopEnd:
        data = clisock.recv(2048)
        if t==0:
			print data
			num = data[6]
        clisock.send(data)
        t+=1
	
	if not data:
	   clisock.shutdown(0)
           listeClient.remove(clisock)
	   print "Le client"+num+" a recu sa commande"
	   loopEnd = False

	
	


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',8001))
sock.listen(5)
while True:
	clisock, addr = sock.accept()
	listeClient.append(clisock)
	print "Un client a passe commande"
	t = threading.Thread(target=f_thread, args=(clisock,))
	t.start()


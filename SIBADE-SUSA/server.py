from socket import *
import sys, threading, os, os.path, re, datetime, configparser
#import spaceX
from spaceX import Map

if len(sys.argv) != 1:
    print(f"Usage: {sys.argv[0]}")
    sys.exit(1)
	
def quiter():
	...

def switch(cmd):
	print(cmd)
	x = cmd.split()[0].upper()
	print(x)
	"""
	return {
        'QUIT': quiter(),
    }.get(x, "4000")
	"""

# Prog principal

#lecture fichier conf
config = configparser.ConfigParser()
config.read('spaceXserv.conf')

#creation socket
sock_server = socket()
sock_server.bind(("", (int)(config['DEFAULT']['port'])))
sock_server.listen(4)

mapServ = Map()

with open(config['DEFAULT']['log'], "a") as logFic:
	logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Serveur en attente sur le port " + config['DEFAULT']['port'])


while True:
	try:
		sock_client, adr_client = sock_server.accept() 
		with open(config['DEFAULT']['log'], "a") as logFic:
			logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Connexion de " + adr_client[0])

		cmd = sock_client.recv(255)
		switch(cmd)
		print(mapServ)
		#return nouvelle Map
	except KeyboardInterrupt:
		break
		
		
sock_server.shutdown(SHUT_RDWR)
with open(config['DEFAULT']['log'], "a") as logFic:
	logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Arret serveur")

for t in threading.enumerate():
	if t != threading.main_thread(): t.join
sys.exit(0)

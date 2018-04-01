from socket import *
import sys, threading, os, os.path, re

if len(sys.argv) != 3:
	print("Usage: {} <port> <répertoire>".format(sys.argv[0]))
	sys.exit(1)
	
DOC_ROOT = os.path.realpath(sys.argv[2]) # Répertoire racine du serveur

def traiter_client(client):
	wrapper = client.makefile()
	ligne = wrapper.readline()[:-1] # [:-1] pour ôter le \n terminal
	# switch(ligne): ?
	client.close()

# Prog principal
sock_server = socket()
sock_server.bind(("", int(sys.argv[1])))
sock_server.listen(4)
print("le serveur écoute sur le port " + sys.argv[1], file=sys.stderr)
print("Son répertoire de base est " + DOC_ROOT, file=sys.stderr)

while True:
	try:
		sock_client, adr_client = sock_server.accept()
		print("Connexion de ".format(adr_client[0]))
		threading.Thread(target=traiter_client, args=(sock_client,)) \
		.start()
	except KeyboardInterrupt:
		break
		
		
sock_server.shutdown(SHUT_RDWR)
print("Arrêt du serveur")
for t in threading.enumerate():
	if t != threading.main_thread(): t.join
sys.exit(0)

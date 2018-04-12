from socket import *
import sys, threading, os, os.path, re, datetime, configparser
from spaceX import Map,Robot

if len(sys.argv) != 1:
    print(f"Usage: {sys.argv[0]}")
    sys.exit(1)

def initRobot(client):
    mapServ.listRobot[client] = Robot(0,0,"newRobot")

def quiter(client):
	mapServ.listRobot[client].actif = False
	with open(config['DEFAULT']['log'], "a") as logFic:
		logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1011")
	return "1011"

def rename(client,cmd):
    newName = cmd.decode("utf-8").split()
    if len(newName) != 2 :
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 3021")
        return "3021"
    for rob in mapServ.listRobot:
        if mapServ.listRobot[rob].name == newName[1]:
            with open(config['DEFAULT']['log'], "a") as logFic:
                logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 2021")
            return "2021"

    mapServ.listRobot[client].name = newName[1]
    print(mapServ.listRobot[client])
    with open(config['DEFAULT']['log'], "a") as logFic:
        logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1021")
    return "1021"

def send(client,cmd):
    return "3030"

def pause(client):
    if mapServ.listRobot[client].actif:
        mapServ.listRobot[client].actif = False
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1041")
        return "1041"
    else:
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 2041")
        return "2041"

def unpause(client):
    if mapServ.listRobot[client].actif:
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 2051")
        return "1041"
    else:
        mapServ.listRobot[client].actif = True
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1051")
        return "2041"

def status(client):
    return "6"

def info(client):
    info = "\n"
    if len(mapServ.listRobot) == 0 :
        info = "no robots found"
    else:
        for rob in mapServ.listRobot:
            info += str(mapServ.listRobot[rob]) + "\n"
    with open(config['DEFAULT']['log'], "a") as logFic:
	    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1071")
    return "1071_"+info

def move(client,cmd):
    return "8"

def switch(client,cmd):
    x = cmd.decode("utf-8").split()[0].upper()
    with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Commande " + x + " par " + client )
    return {
        'QUIT': quiter(client),
        'RENAME': rename(client,cmd),
        'SEND': send(client,cmd),
        'PAUSE': pause(client),
        'UNPAUSE': unpause(client),
        'STATUS': status(client),
        'INFO': info(client),
        'MOVE': move(client,cmd)
    }.get(x, "4000")

# Prog principal

#lecture fichier conf
config = configparser.ConfigParser()
config.read('spaceX.conf')

#creation socket
sock_server = socket()
sock_server.bind(("", (int)(config['DEFAULT']['port'])))
sock_server.listen(4)

mapServ = Map()

with open(config['DEFAULT']['log'], "a") as logFic:
    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Serveur en attente sur le port " + config['DEFAULT']['port'])

sock_client, adr_client = sock_server.accept()

#nouvelle connexion = nouveau robot
if adr_client[0] not in mapServ.listRobot :
    initRobot(adr_client[0])

while True:
    try:
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Connexion de " + adr_client[0])

        cmd = sock_client.recv(255)
        rep = switch(adr_client[0],cmd)
        print(rep)
        print(mapServ)
        #return nouvelle Map
        sock_server.sendto(rep.encode(), adr_client)

    except KeyboardInterrupt:
        break


sock_server.shutdown(SHUT_RDWR)
with open(config['DEFAULT']['log'], "a") as logFic:
    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Arret serveur")

for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)

from socket import *
import sys, threading, os, os.path, re, datetime, configparser
from spaceX import Map,Robot

if len(sys.argv) != 1:
    print(f"Usage: {sys.argv[0]}")
    sys.exit(1)

def initRobot():
    mapServ.listRobot[client] = Robot(0,0,"newRobot")

def quiter(client):
    for rob in mapServ.listRobot:
        if rob.name == newName:
            rob.actif = False

    with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1011")
    return "1011"

def rename(client,cmd):
    ret = ""
    newName = cmd.decode("utf-8").split()
    if newName.len != 2 :
        ret = "3021"
    for rob in mapServ.listRobot:
        if rob.name == newName:
            ret = "2021"

    mapServ.listRobot[client].name = newName[1]
    ret = "1021"

    with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse " + rep)
    return ret

def send(client,cmd):
    return "3"

def pause(client):
    return "4"

def unpause(client):
    return "5"

def status(client):
    return "6"

def info(client):
    info = "\n"
    if mapServ.listRobot.len == 0 :
        info = "no robots found"
    else:
        for rob in mapServ.listRobot:
            info += rob.name + "("+("Actif" if rob.actif else "Inactif")+")"+" : [" + rob.posX + "," + rob.posY + "]" + rob.ress + " ressource(s)" + "\n"
    with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse 1071")
    return "1071_"+info

def move(client,cmd):
    return "8"

def switch(client,cmd):
    x = cmd.decode("utf-8").split()[0].upper()
    with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Commande " + x[0] + " par " + client )
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
config.read('spaceXserv.conf')

#creation socket
sock_server = socket()
sock_server.bind(("", (int)(config['DEFAULT']['port'])))
sock_server.listen(4)

mapServ = Map()

with open(config['DEFAULT']['log'], "a") as logFic:
    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Serveur en attente sur le port " + config['DEFAULT']['port'])

print('avant accept')
sock_client, adr_client = sock_server.accept()
print(' apres accept')

#nouvelle connexion = nouveau robot
print(mapServ.listRobot.keys())
print(adr_client)
'''
if adr_client[0] not in mapServ.listRobot.keys()
    initRobot()
'''
while True:
    try:
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Connexion de " + adr_client[0])

        cmd = sock_client.recv(255)
        print(switch(adr_client[0],cmd))
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

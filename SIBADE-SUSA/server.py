from socket import *
import sys, threading, os, os.path, re, datetime, configparser, time
from lib import Map,Robot
"""
if len(sys.argv) != 1:
    print(f"Usage: {sys.argv[0]}")
    sys.exit(1)
"""
def updateLog(code):
	with open(config['DEFAULT']['log'], "a") as logFic:
		logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Reponse " + code)

def initRobot(client):
    mapServ.listRobot[client] = Robot(0,0,"newRobot")

def rename(client,cmd):
    newName = cmd.decode("utf-8").split()
    if len(newName) != 2 :
        return "3021"
    for rob in mapServ.listRobot:
        if mapServ.listRobot[rob].name == newName[1]:
            return "2021"

    mapServ.listRobot[client].name = newName[1]
    return "1021"

def send(client,cmd):
    return "3030"

def pause(client):
    if mapServ.listRobot[client].actif:
        mapServ.listRobot[client].actif = False
        return "1041"
    else:
        return "2041"

def unpause(client):
    if mapServ.listRobot[client].actif:
        return "2051"
    else:
        mapServ.listRobot[client].actif = True
        return "1051"

def status(client):
    return "1061_\n"+str(mapServ.listRobot[client])

def info(client):
    info = "\n"
    if len(mapServ.listRobot) == 0 :
        info = "no robots found"
    else:
        for rob in mapServ.listRobot:
            if mapServ.listRobot[rob].actif:
                info += str(mapServ.listRobot[rob]) + "\n"
    return "1071_"+info

def move(client,cmd,mapServ):
	direc = cmd.decode("utf-8").split()

	if len(direc) != 2 :
		return "3081"
	if direc[1].upper() not in {'U','D','L','R'}:
		return "3082"

	newCoord = (0,0)

	if direc[1].upper() == 'U':
		newCoord = (-1,0)
	if direc[1].upper() == 'D':
		newCoord = (1,0)
	if direc[1].upper() == 'L':
		newCoord = (0,-1)
	if direc[1].upper() == 'R':
		newCoord = (0,1)

	oldCoord = (mapServ.listRobot[client].posX,mapServ.listRobot[client].posY)

	if mapServ.getPos((newCoord[0]+oldCoord[0]),(newCoord[1]+oldCoord[1])).isObs or newCoord[0]+oldCoord[0] < 0 or newCoord[0]+oldCoord[0] > 11 or newCoord[1]+oldCoord[1] < 0 or newCoord[1]+oldCoord[1] > 10 :
		return "2081"
	else:
		if mapServ.getPos((newCoord[0]+oldCoord[0]),(newCoord[1]+oldCoord[1])).isRess:
			mapServ.listRobot[client].ress += 1
			mapServ.getPos((newCoord[0]+oldCoord[0]),(newCoord[1]+oldCoord[1])).isRess = False
		mapServ.listRobot[client].posX = (newCoord[0]+oldCoord[0])
		mapServ.listRobot[client].posY = (newCoord[1]+oldCoord[1])
		return "1081"

def quiter(client):
	mapServ.listRobot[client].actif = False
	return "1011"

def switch(client,cmd,mapServ):
	x = cmd.decode("utf-8").split()[0].upper()
	with open(config['DEFAULT']['log'], "a") as logFic:
		logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Commande " + x + " par " + (str)(client) )
	return {
        #'QUIT': quiter(client),
        'RENAME': rename(client,cmd),
        'SEND': send(client,cmd),
        'PAUSE': pause(client),
        'UNPAUSE': unpause(client),
        'STATUS': status(client),
        'INFO': info(client),
        'MOVE': move(client,cmd,mapServ)
    }.get(x, "4000")

# Prog principal

#lecture fichier conf
config = configparser.ConfigParser()
config.read('spaceX.conf')

#creation socket
"""
sock_server = socket()
sock_server.bind(("", (int)(config['DEFAULT']['port'])))
sock_server.listen(4)
"""
sock_server = socket(AF_INET, SOCK_DGRAM)
sock_server.bind(('', (int)(config['DEFAULT']['port'])))

mapServ = Map()
initTimer = time.time()

with open(config['DEFAULT']['log'], "a") as logFic:
    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Serveur en attente sur le port " + config['DEFAULT']['port'])

#sock_client, adr_client = sock_server.accept()

#nouvelle connexion = nouveau robot
"""
if adr_client[0] not in mapServ.listRobot :
    initRobot(adr_client[0])
"""
while True:
    try:
        print("entre")
        with open(config['DEFAULT']['log'], "a") as logFic:
            logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Connexion de " ) #+ adr_client[0]

        cmd = sock_server.recvfrom(255)
        (mess , uneIP) = cmd

        if uneIP not in mapServ.listRobot :
            initRobot(uneIP)

        #rep = switch(adr_client[0],cmd,mapServ)
        rep = switch(uneIP,mess,mapServ)
        actualTimer = time.time()
        print(initTimer,actualTimer,actualTimer-initTimer)
        #if actualTimer - initTimer > 300 : #5min
        if actualTimer - initTimer > 60 :
            mapServ.refreshRess()
            initTimer=time.time()
        print(rep)
        print(mapServ)
        #print(mapServ.listRobot[adr_client[0]])
        print("_____")
        updateLog(rep.split("_")[0])
        print(uneIP)
        #print(adr_client)
        print(rep)
        sock_server.sendto(rep.encode(), uneIP)

    except KeyboardInterrupt:
        break


sock_server.shutdown(SHUT_RDWR)
with open(config['DEFAULT']['log'], "a") as logFic:
    logFic.write("\n" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " Arret serveur")

for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)

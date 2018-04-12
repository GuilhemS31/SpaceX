from socket import *
from datetime import *
from spaceX import *
import sys, locale
import json

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <port>", file="sys.stderr")
    sys.exit(1)

TAILLE_TAMPON = 256

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', int(sys.argv[1])))
file = open("server.log","a")
file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Server started \n")
file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Listen on :{sys.argv[1]} \n")
file.close()

map_server = Map(11,11)
map_server.add_obstacle(Obstacle(1,2))
map_server.add_obstacle(Obstacle(3,8))
map_server.add_obstacle(Obstacle(5,5))
map_server.add_obstacle(Obstacle(4,3))
map_server.add_obstacle(Obstacle(7,10))
map_server.add_obstacle(Obstacle(6,1))
map_server.add_obstacle(Obstacle(9,4))

def rename_cmd(reponse):
    if len(reponse) == 2:
        return map_server.get_robot(ip_client).rename(reponse[1])
    return '3021 Missing argument (usage : rename <name>)'

def move_cmd(reponse):
    if len(reponse) == 2:
        return map_server.move_robot(ip_client, reponse[1])
    return '3081 Missing argument : direction (usage : move <direction>)'

def status_cmd(adresse_client):
    return map_server.status(adresse_client)

def pause_cmd(adresse_client):
    return map_server.pause_robot(adresse_client)

def unpause_cmd(adresse_client):
    return map_server.unpause_robot(adresse_client)

def jdefault(object):
    return object.__dict__


while True:
    try:
        requete = sock.recvfrom(TAILLE_TAMPON)
        (mess, adr_client) = requete
        ip_client, port_client = adr_client
        file = open("server.log","a")
        file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Received {mess.decode()} from {ip_client}:{port_client}\n")
        file.close()
        if map_server.client_exists(ip_client) == False:
            map_server.add_robot(ip_client, Robot('undefined', 4, 8))
        reponse = mess.decode().split(' ')

        rep = ''

        if reponse[0] == 'help':
            rep = f'Commands : quit, rename, send, pause, unpause, status, info'
        elif reponse[0] == 'info':
            rep = str(map_server)
        elif reponse[0] == 'move':
            rep = move_cmd(reponse)
        elif reponse[0] == 'rename':
            rep = rename_cmd(reponse)
        elif reponse[0] == 'send':
            rep = 'coucou'
        elif reponse[0] == 'pause':
            rep = pause_cmd(ip_client)
        elif reponse[0] == 'unpause':
            rep = unpause_cmd(ip_client)
        elif reponse[0] == 'status':
            rep = status_cmd(ip_client)
        else:
            rep = f'200 Incorrect request : {reponse[0]}'
        rep = "> " + rep + "\n"
        file = open("map.json", "w")
        file.write(json.dumps(map_server, default=jdefault))
        file.close()

        sock.sendto(rep.encode(), adr_client)
    except KeyboardInterrupt: break

file = open("server.log", "a")
file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Server stopped...\n")
file.close()

sock.close()
sys.exit(0)

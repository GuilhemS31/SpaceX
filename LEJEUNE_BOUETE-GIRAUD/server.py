from socket import *
from datetime import *
from spaceX import *
import sys, locale

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
    return 'Missing argument (usage : rename <name>)'

def move_cmd(reponse):
    if len(reponse) == 2:
        return map_server.move_robot(ip_client, reponse[1])
    return 'Missing argument : direction (usage : move <direction>)'

def status_cmd(adresse_client):
    return map_server.status(adresse_client)


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
            rep = f'100 Commands : quit, rename, send, pause, unpause, status, info'
        elif reponse[0] == 'info':
            rep = f'100 '+str(map_server)
        elif reponse[0] == 'move':
            rep = f'100 '+move_cmd(reponse)
        elif reponse[0] == 'rename':
            rep = f'100 '+rename_cmd(reponse)
        elif reponse[0] == 'send':
            rep = f'coucou'
        elif reponse[0] == 'pause':
            rep = f'coucou'
        elif reponse[0] == 'unpause':
            rep = f'coucou'
        elif reponse[0] == 'status':
            rep = f'100 '+status_cmd(ip_client)
        else:
            rep = f'200 Requête incorrecte : {reponse[0]}'

        sock.sendto(rep.encode(), adr_client)
    except KeyboardInterrupt: break

file = open("server.log", "a")
file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Server stopped...\n")
file.close()

sock.close()
sys.exit(0)

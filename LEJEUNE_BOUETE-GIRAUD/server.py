from socket import *
from datetime import *
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
while True:
    try:
        requete = sock.recvfrom(TAILLE_TAMPON)
        (mess, adr_client) = requete
        ip_client, port_client = adr_client
        file = open("server.log","a")
        file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Received {mess.decode()} from {ip_client}:{port_client}\n")
        file.close()
        reponse = mess.decode().upper()
        commandes = {'HELP' : 'Commands list : quit, rename, send, pause, unpause, status, info, move'}
        if reponse in commandes:
            rep = f'100 {commandes[reponse]}'
            sock.sendto(rep.encode(), adr_client)
        else:
            erreur = f'200 Requête incorrecte : {reponse}'
            sock.sendto(erreur.encode(), adr_client)
    except KeyboardInterrupt: break

file = open("server.log", "a")
file.write(f"{date.today().strftime('%Y/%m/%d')} {datetime.today().strftime('%X')} Server stopped...\n")
file.close()

sock.close()
sys.exit(0)

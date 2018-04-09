from socket import *
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ip> <port>", file=sys.stderr)
    sys.exit(1)

TAILLE_TAMPON = 256

print("Enter a command (help to see the list, quit to leave the program) : ")
with socket(AF_INET, SOCK_DGRAM) as sock:
    while True:
        message = input("> ")
        if message == "quit" :
            print("Disconnected successful")
            break
        sock.sendto(message.encode(), (sys.argv[1], int(sys.argv[2])))
        reponse, _ = sock.recvfrom(TAILLE_TAMPON)
        print(reponse.decode())

from socket import *
from interfacev2 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ip> <port>", file=sys.stderr)
    sys.exit(1)
TAILLE_TAMPON = 256

with socket(AF_INET, SOCK_DGRAM)as sock:
    while True:
        # Remarque : pas besoin de bind car le port local est choisi par le système
        mess = input("$=> ")

        if (mess == "quit"):
            print("Merci d'avoir utiliser serveur client,  Aurevoir")
            exit(0)
        # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
        sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
        # Réception de la réponse du serveur et décodage de bytes en str
        reponse, _ = sock.recvfrom(TAILLE_TAMPON)
        print("Réponse = " + reponse.decode())


@QtCore.pyqtSlot()
def on_Send_clicked(self):
    mess = self.Command.text()
    if (mess == "quit"):
        print("Merci d'avoir utiliser serveur client,  Aurevoir")
        exit(0)
    # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
    sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
    # Réception de la réponse du serveur et décodage de bytes en str
    reponse, _ = sock.recvfrom(TAILLE_TAMPON)
    print("Réponse = " + reponse.decode())

class MaWin(QtGui, Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.__init__(self, parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MaWin()#QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

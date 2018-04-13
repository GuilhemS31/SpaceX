from socket import *
from interfacev2 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys, configparser

config = configparser.ConfigParser()
config.read('spaceX.conf')

TAILLE_TAMPON = 256

class MaWin(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        print("ici")


    @QtCore.pyqtSlot()
    def on_Send_clicked(self):
        print("click")
        with socket(AF_INET, SOCK_DGRAM) as sock:
            mess = ui.Command.text()
            print("click1")
            text =  ui.Terminal.toPlainText() +"> "+ mess +"\n"
            print("click2")
            ui.Terminal.setText(text)
            if mess != "":
                print("click3")
                if (mess == "quit"):
                    sock.sendto(mess.encode(), ((config['DEFAULT']['ip']), (int)(config['DEFAULT']['port'])))
                    print("Merci d'avoir utiliser serveur client,  Aurevoir")
                    exit(0)
                ui.Command.clear()
                print("click4")
                # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
                sock.sendto(mess.encode(), ((config['DEFAULT']['ip']), (int)(config['DEFAULT']['port'])))
                print("click5")
                # Réception de la réponse du serveur et décodage de bytes en str
                reponse, _ = sock.recvfrom(TAILLE_TAMPON)
                rep = reponse.decode()
                print("click6")
                ui.Terminal.setText(ui.Terminal.toPlainText() + rep + "\n")

    #MaWin.Send.clicked.connect(on_Send_clicked)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Form = QtWidgets.QWidget()
    MainWindow = MaWin()#QtWidgets.QMainWindow()

    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    ui.Send.clicked.connect(MaWin.on_Send_clicked)

    #ui.setupUi(Form)
    MainWindow.show()
    #Form.show()
    sys.exit(app.exec_())

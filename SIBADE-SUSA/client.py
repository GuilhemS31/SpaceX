from socket import *
from interfacev2 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys, configparser

config = configparser.ConfigParser()
config.read('spaceX.conf')

TAILLE_TAMPON = 1024

class MaWin(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        print("ici")


    @QtCore.pyqtSlot()
    def on_Send_clicked(self):
        with socket(AF_INET, SOCK_DGRAM) as sock:
            mess = ui.Command.text()
            text =  ui.Terminal.toPlainText() +"> "+ mess +"\n"
            ui.Terminal.setText(text)
            if mess != "":
                if (mess == "quit"):
                    sock.sendto(mess.encode(), ((config['DEFAULT']['ip']), (int)(config['DEFAULT']['port'])))
                    print("Merci d'avoir utiliser SpaceX,  Aurevoir")
                    exit(0)
                ui.Command.clear()
                # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
                sock.sendto(mess.encode(), ((config['DEFAULT']['ip']), (int)(config['DEFAULT']['port'])))
                # Réception de la réponse du serveur et décodage de bytes en str
                reponse, _ = sock.recvfrom(TAILLE_TAMPON)
                rep = reponse.decode()
                rText =  rep.split("#")[0]
                rMap = rep.split("#")[1]
                ui.Terminal.setText(ui.Terminal.toPlainText() + rText + "\n")
                ui.vueTable.setText(rMap)




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

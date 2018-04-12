from socket import *
from PyQt4 import QtGui, QtCore
from interface import Ui_MainWindow
import sys

if len(sys.argv) != 3:
    print("Usage: "+sys.argv[0]+" <ip> <port>", file=sys.stderr)
    sys.exit(1)

class MaWin(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.textBrowser.setText("Enter a command (help to see the list, quit to leave the program) : \n")

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        TAILLE_TAMPON = 256
        with socket(AF_INET, SOCK_DGRAM) as sock:
            message = self.lineEdit.text()
            if message == "quit" :
                self.textBrowser.setText("1011 Disconnected successful")
                sys.exit(0)
            self.lineEdit.setText("")
            sock.sendto(message.encode(), (sys.argv[1], int(sys.argv[2])))
            reponse, _ = sock.recvfrom(TAILLE_TAMPON)
            rep = self.textBrowser.toPlainText() + reponse.decode()
            self.textBrowser.setText(rep)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MaWin()
    win.show()
    sys.exit(app.exec_())

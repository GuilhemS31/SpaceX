from socket import *
from PyQt4 import QtGui, QtCore
from interface import Ui_MainWindow
import sys

"""class MaWin(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MaWin()
    win.show()
    sys.exit(app.exec_())"""

if len(sys.argv) != 3:
    print("Usage: "+sys.argv[0]+" <ip> <port>", file=sys.stderr)
    sys.exit(1)

TAILLE_TAMPON = 256

print("Enter a command (help to see the list, quit to leave the program) : ")
with socket(AF_INET, SOCK_DGRAM) as sock:
    while True:
        message = input("> ")
        if message == "quit" :
            print("1011 Disconnected successful")
            break
        sock.sendto(message.encode(), (sys.argv[1], int(sys.argv[2])))
        reponse, _ = sock.recvfrom(TAILLE_TAMPON)
        print(reponse.decode())

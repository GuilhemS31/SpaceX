from socket import *
from PyQt4 import QtGui, QtCore
from interface import Ui_MainWindow
import sys
import json

if len(sys.argv) != 3:
    print("Usage: "+sys.argv[0]+" <ip> <port>", file=sys.stderr)
    sys.exit(1)

class MaWin(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.textBrowser.setText("Enter a command (help to see the list, quit to leave the program) : \n")
        self.refresh_map(open("map.json","r").read())

    def refresh_map(self, map_server):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        _map = json.loads(map_server)
        self.gridLayout.rowCount = _map['lines']
        self.gridLayout.columnCount = _map['columns']
        for obstacle in _map['obstacles_list']:
            self.gridLayout.addWidget(QtGui.QPushButton('O'), obstacle['line'], obstacle['column'])
        for robot in _map['robots_list'].values():
            self.gridLayout.addWidget(QtGui.QPushButton(robot['username']), robot['line'], robot['column'])


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
            self.refresh_map(open("map.json","r").read())


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MaWin()
    win.show()
    sys.exit(app.exec_())

################################################################################
#                                                                              #
################################################################################

import sys
from PyQt4 import QtGui


################################################################################
#                                                                              #
################################################################################
class Win(QtGui.QMainWindow):

    def __init__(self):
        super(Win, self).__init__()
        self.initWin()
        self.initTopBar()
        self.initPicArea()
        self.show()


    def initWin(self):
        self.win_w = 900
        self.win_h = 500
        self.pic_s = 400

        self.setGeometry(300, 300, self.win_w, self.win_h)
        self.setWindowTitle('FYO2013')


    def initTopBar(self):
        openAction = QtGui.QAction(QtGui.QIcon('img\open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open new file')
        openAction.triggered.connect(self.showDialog)

        exitAction = QtGui.QAction(QtGui.QIcon('img\exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)


    def initPicArea(self):
        picsWidget = QtGui.QWidget(self)
        picsWidget.setFixedSize(self.pic_s, self.pic_s)
        self.setCentralWidget(picsWidget)
        src_pic = QtGui.QPixmap('img\lena.png')
        src = QtGui.QLabel(picsWidget)
        src.setPixmap(src_pic)
        src.setFixedSize(src_pic.size())




    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if (fname):
            f = open(fname, 'r')
            with f:
                data = f.read()
                print (data)


################################################################################
# MAIN                                                                         #
################################################################################

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

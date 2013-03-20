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
        self.win_w = 1050
        self.win_h = 500
        self.pic_s = 500

        self.setGeometry(150, 150, self.win_w, self.win_h)
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

        highPassFilterAction = QtGui.QAction('&High-Pass Filter', self)
        highPassFilterAction.setCheckable(True)
        lowPassFilterAction = QtGui.QAction('&Low-Pass Filter', self)
        lowPassFilterAction.setCheckable(True)
        customFilterAction = QtGui.QAction('&Custom Filter',self)
        customFilterAction.setCheckable(True)

        predefinedFilterMenu = QtGui.QMenu('&Active', self)
        predefinedFilterMenu.addAction(lowPassFilterAction)
        predefinedFilterMenu.addAction(highPassFilterAction)
        predefinedFilterMenu.addAction(customFilterAction)
        createFilterAction = QtGui.QAction('&Create new', self)
        createFilterAction.triggered.connect(self.addFilter)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
        filterMenu = menubar.addMenu('&Filter')
        filterMenu.addMenu(predefinedFilterMenu)
        filterMenu.addAction(createFilterAction)


    def initPicArea(self):
        picsWidget = QtGui.QWidget(self)
        picsWidget.setFixedSize(self.pic_s*2, self.pic_s)
        picsLayout = QtGui.QHBoxLayout()
        picsWidget.setLayout(picsLayout)
        self.setCentralWidget(picsWidget)

        self.src = QtGui.QLabel(picsWidget)
        picsLayout.addWidget(self.src)
        self.dst = QtGui.QLabel(picsWidget)
        picsLayout.addWidget(self.dst)


    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
        if (fname):
            self.openPicture(fname)

    def openPicture(self, pic_file):
        src_pic = QtGui.QPixmap(pic_file)
        self.src.setPixmap(src_pic)
        self.src.setFixedSize(src_pic.size())
        dst_pic = QtGui.QPixmap(pic_file)
        self.dst.setPixmap(dst_pic)
        self.dst.setFixedSize(dst_pic.size())


    def addFilter(self):
        print ("add filter")


    def removeFilter(self):
        print ("remove filter")


################################################################################
# MAIN                                                                         #
################################################################################

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

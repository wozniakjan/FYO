################################################################################
#                                                                              #
################################################################################

import sys, numpy
from PyQt4 import QtGui
from PIL import Image


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
        self.win_w = 640
        self.win_h = 640
        self.pic_s = 300

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
        picsWidget.setFixedSize(self.pic_s*2+50, self.pic_s*2+50)
        picsLayout = QtGui.QGridLayout()

        self.src = QtGui.QLabel(picsWidget)
        self.src.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.src, 1, 0)
        picsLayout.addWidget(QtGui.QLabel('Source picture'), 0, 0)
        self.dst = QtGui.QLabel(picsWidget)
        self.dst.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.dst, 1, 1)
        picsLayout.addWidget(QtGui.QLabel('Filtered picture'), 0, 1)

        self.flt = QtGui.QLabel(picsWidget)
        self.flt.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.flt, 3, 0)
        picsLayout.addWidget(QtGui.QLabel('Filter picture'), 2, 0)
        self.fft = QtGui.QLabel(picsWidget)
        self.fft.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.fft, 3, 1)
        picsLayout.addWidget(QtGui.QLabel('Fourier transform picture'), 2, 1)

        picsWidget.setLayout(picsLayout)
        picsLayout.setColumnStretch(0,1)
        picsLayout.setRowStretch(1,1)
        picsLayout.setRowStretch(3,1)
        self.setCentralWidget(picsWidget)

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
        if (fname):
            self.openPicture(fname)

    def openPicture(self, pic_file):
        src_pic = QtGui.QPixmap(pic_file)
        self.src.setPixmap(src_pic.scaled(self.pic_s, self.pic_s))

#        i = Image.open(pic_file)
#        j = numpy.fft.fft2(i)
#        imshow(real(j))

        i = Image.open(pic_file)
        i = i.convert('L')
        i = numpy.asarray(i)
        i_fft = numpy.fft.fftshift(numpy.fft.fft2(i))
        i_fft2 = abs(numpy.real(i_fft))

        for i in range(0,512):
            for j in range(0,512):
                i_fft2[i][j] /= 100
                if i_fft2[i][j] > 255:
                    i_fft2[i][j] = 255


        i_ifft = numpy.fft.ifft2(numpy.fft.ifftshift(i_fft))

        Image.fromarray(numpy.uint8(i_fft2)).save("img/fft_temp.png")
        fft_pic = QtGui.QPixmap('img/fft_temp.png')
        self.fft.setPixmap(fft_pic.scaled(self.pic_s, self.pic_s))
        self.fft.setFixedSize(self.pic_s,self.pic_s)

        Image.fromarray(numpy.uint8(numpy.real(i_ifft))).save("img/ifft_temp.png")
        ifft_pic = QtGui.QPixmap('img/ifft_temp.png')
        self.dst.setPixmap(ifft_pic.scaled(self.pic_s, self.pic_s))
        self.dst.setFixedSize(self.pic_s,self.pic_s)

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

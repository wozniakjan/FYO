################################################################################
#                                                                              #
################################################################################

import sys, numpy
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PIL import Image

HIGH_PASS1 = 0
HIGH_PASS2 = 1
HIGH_PASS5 = 2
HIGH_PASS10 = 3
LOW_PASS10 = 4
LOW_PASS20 = 5
LOW_PASS30 = 6
LOW_PASS40 = 7
RECT10 = 8
RECT20 = 9
RECT30 = 10
RECT40 = 11
INV_RECT10 = 12
INV_RECT20 = 13
INV_RECT30 = 14
INV_RECT40 = 15
MAX = 16

################################################################################
#                                                                              #
################################################################################
class Win(QMainWindow):

    def __init__(self):
        super(Win, self).__init__()
        self.initWin()
        self.initTopBar()
        self.initPicArea()
        self.im_fft = "null"
        self.show()


    def initWin(self):
        self.win_w = 640
        self.win_h = 640
        self.pic_s = 300

        self.setGeometry(150, 150, self.win_w, self.win_h)
        self.setWindowTitle('FYO2013')


    def initTopBar(self):
        openAction = QAction(QIcon('img/open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open new file')
        openAction.triggered.connect(self.showDialog)

        exitAction = QAction(QIcon('img/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.filterAction = []
        self.filterAction.append(QAction('&High-Pass Filter r=1px', self))
        self.filterAction[HIGH_PASS1].setCheckable(True)
        self.filterAction[HIGH_PASS1].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&High-Pass Filter r=2px', self))
        self.filterAction[HIGH_PASS2].setCheckable(True)
        self.filterAction[HIGH_PASS2].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&High-Pass Filter r=5px', self))
        self.filterAction[HIGH_PASS5].setCheckable(True)
        self.filterAction[HIGH_PASS5].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&High-Pass Filter r=10px', self))
        self.filterAction[HIGH_PASS10].setCheckable(True)
        self.filterAction[HIGH_PASS10].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Low-Pass Filter r=10px', self))
        self.filterAction[LOW_PASS10].setCheckable(True)
        self.filterAction[LOW_PASS10].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Low-Pass Filter r=20px', self))
        self.filterAction[LOW_PASS20].setCheckable(True)
        self.filterAction[LOW_PASS20].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Low-Pass Filter r=40px', self))
        self.filterAction[LOW_PASS30].setCheckable(True)
        self.filterAction[LOW_PASS30].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Low-Pass Filter r=80px', self))
        self.filterAction[LOW_PASS40].setCheckable(True)
        self.filterAction[LOW_PASS40].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Rectangle Filter a=10px',self))
        self.filterAction[RECT10].setCheckable(True)
        self.filterAction[RECT10].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Rectangle Filter a=20px',self))
        self.filterAction[RECT20].setCheckable(True)
        self.filterAction[RECT20].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Rectangle Filter a=40px',self))
        self.filterAction[RECT30].setCheckable(True)
        self.filterAction[RECT30].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Rectangle Filter a=80px',self))
        self.filterAction[RECT40].setCheckable(True)
        self.filterAction[RECT40].triggered.connect(self.setFilter) 
        self.filterAction.append(QAction('&Inverse Rectangle Filter a=10px',self))
        self.filterAction[INV_RECT10].setCheckable(True)
        self.filterAction[INV_RECT10].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Inverse Rectangle Filter a=20px',self))
        self.filterAction[INV_RECT20].setCheckable(True)
        self.filterAction[INV_RECT20].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Inverse Rectangle Filter a=40px',self))
        self.filterAction[INV_RECT30].setCheckable(True)
        self.filterAction[INV_RECT30].triggered.connect(self.setFilter)
        self.filterAction.append(QAction('&Inverse Rectangle Filter a=80px',self))
        self.filterAction[INV_RECT40].setCheckable(True)
        self.filterAction[INV_RECT40].triggered.connect(self.setFilter)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
        filterMenu = menubar.addMenu('&Filter')
        for i in range(HIGH_PASS1, MAX):
            filterMenu.addAction(self.filterAction[i])


    def initPicArea(self):
        picsWidget = QWidget(self)
        picsWidget.setFixedSize(self.pic_s*3+60, self.pic_s*2+60)
        picsLayout = QGridLayout()

        self.src = QLabel(picsWidget)
        self.src.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.src, 1, 0)
        picsLayout.addWidget(QLabel('Picture'), 0, 0, Qt.AlignHCenter)
        self.dst = QLabel(picsWidget)
        self.dst.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.dst, 1, 2)
        picsLayout.addWidget(QLabel('Filtered picture'), 0, 2, Qt.AlignHCenter)

        self.filter = QLabel(picsWidget)
        self.filter.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.filter, 3, 1)
        picsLayout.addWidget(QLabel('Filter'), 2, 1, Qt.AlignHCenter)

        self.fft = QLabel(picsWidget)
        self.fft.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.fft, 3, 0)
        picsLayout.addWidget(QLabel('Fourier transform'), 2, 0, Qt.AlignHCenter)
        self.fft2 = QLabel(picsWidget)
        self.fft2.setFixedSize(self.pic_s,self.pic_s)
        picsLayout.addWidget(self.fft2, 3, 2)
        picsLayout.addWidget(QLabel('Fourier transform filtered'), 2, 2, Qt.AlignHCenter)
        
        picsWidget.setLayout(picsLayout)
        picsLayout.setColumnStretch(0,1)
        picsLayout.setRowStretch(1,1)
        picsLayout.setRowStretch(3,1)
        self.setCentralWidget(picsWidget)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './pictures/')
        if (fname):
            self.openPicture(fname)

    def openPicture(self, pic_file):
        self.statusBar().showMessage('Opening picture')
        filters = len(self.filterAction)
        for i in range(0,filters):
            self.filterAction[i].setChecked(False)
    
        src_pic = QPixmap(pic_file)
        self.src.setPixmap(src_pic.scaled(self.pic_s, self.pic_s))

        im = Image.open(pic_file)
        im = im.convert('L')
        im = numpy.asarray(im)
        self.im_fft = numpy.fft.fftshift(numpy.fft.fft2(im))
        im_fft_view = self.count_fft_view(self.im_fft, 100)
        self.setFilter()
        
        Image.fromarray(numpy.uint8(im_fft_view)).save("img/fft_temp.png")
        fft_pic = QPixmap('img/fft_temp.png')
        self.fft.setPixmap(fft_pic.scaled(self.pic_s, self.pic_s))
        self.fft.setFixedSize(self.pic_s,self.pic_s)
                
    def count_fft_view(self, im_fft, q):
        im_fft_view = abs(numpy.real(im_fft))
        x = im_fft_view[0].size
        y = int(im_fft_view.size/x)
        print(x, y)
        for i in range(0,y):
            for j in range(0,x):
                im_fft_view[i][j] /= q
                if im_fft_view[i][j] > 255:
                    im_fft_view[i][j] = 255
        return im_fft_view
    
    def setFilter(self):
        print("setFilter()")
        self.statusBar().showMessage('Filtering picture')
        if self.im_fft != "null":
            self.initSumfilter()
            filters = len(self.filterAction)
            for i in range(0,filters):
                if self.filterAction[i].isChecked(): 
                    self.sumFilter(i)    
            self.filterSpectrum()
        self.statusBar().showMessage('')
            
    def filterSpectrum(self):
        print("filterSpectrum()")
        im_fft2 = self.im_fft.copy()
        x = self.im_fft[0].size
        y = int(self.im_fft.size/x)
        for i in range(0,y-1):
            for j in range(0,x-1):
                im_fft2[i][j] = self.im_fft[i][j]*self.sumfilter[i][j]                
        im_fft2_view = self.count_fft_view(im_fft2, 100)
        im_ifft = numpy.fft.ifft2(numpy.fft.ifftshift(im_fft2))
        Image.fromarray(numpy.uint8(im_fft2_view)).save("img/fft2_temp.png")
        fft_pic = QPixmap('img/fft2_temp.png')
        self.fft2.setPixmap(fft_pic.scaled(self.pic_s, self.pic_s))
        self.fft2.setFixedSize(self.pic_s,self.pic_s)
        Image.fromarray(numpy.uint8(numpy.real(im_ifft))).save("img/ifft_temp.png")
        ifft_pic = QPixmap('img/ifft_temp.png')
        self.dst.setPixmap(ifft_pic.scaled(self.pic_s, self.pic_s))
        self.dst.setFixedSize(self.pic_s,self.pic_s)
        self.viewFilter()

    def initSumfilter(self):
        print("initSumfilter()")
        x = self.im_fft[0].size
        y = int(self.im_fft.size/x)
        self.sumfilter = numpy.ndarray(shape=(y,x), dtype=float)
        for i in range(0,y):
            for j in range(0,x):
                self.sumfilter[i][j] = 1
    
    def dist(self, x1, y1, x2, y2):
        dx = x1-x2
        dy = y1-y2
        return numpy.sqrt((dx*dx)+(dy*dy))
        
    def sumFilter(self, i):
        print("sumFilter()")
        x = self.im_fft[0].size
        y = int(self.im_fft.size/x)
        mid_x = x/2
        mid_y = y/2
        
        if (i >= INV_RECT10) & (i<=INV_RECT40):
            s = 10
            if i == INV_RECT10:
                s = 10
            if i == INV_RECT20:
                s = 20
            if i == INV_RECT30:
                s = 40
            if i == INV_RECT40:
                s = 80
            for i in range(0,y):
                for j in range(0,x):
                    if not (i>(mid_y-s))&(i<(mid_y+s))&(j>(mid_x-s))&(j<(mid_x+s)):
                        self.sumfilter[i][j] = 0
        
        if (i >= RECT10) & (i<=RECT40):
            s = 10
            if i == RECT10:
                s = 10
            if i == RECT20:
                s = 20
            if i == RECT30:
                s = 40
            if i == RECT40:
                s = 80
            for i in range(0,y):
                for j in range(0,x):
                    if (i>(mid_y-s))&(i<(mid_y+s))&(j>(mid_x-s))&(j<(mid_x+s)):
                        self.sumfilter[i][j] = 0
        
        if (i >= HIGH_PASS1) & (i<=HIGH_PASS10):
            r = i+1
            for i in range(0,y):
                for j in range(0,x):
                    if (self.dist(j,i,mid_x,mid_y) < r):
                        self.sumfilter[i][j] = 0
        
        if (i >= LOW_PASS10) & (i<=LOW_PASS40):
            r = i
            if i == LOW_PASS10:
                r = 10
            if i == LOW_PASS20:
                r = 20
            if i == LOW_PASS30:
                r = 40
            if i == LOW_PASS40:
                r = 80
            for i in range(0,y):
                for j in range(0,x):
                    if (self.dist(j,i,mid_x,mid_y) > r):
                        self.sumfilter[i][j] = 0   
    
    def viewFilter(self):
        print("viewFilter()")
        x = self.im_fft[0].size
        y = int(self.im_fft.size/x)
        sumfilter_pic2 = numpy.ndarray(shape=(y,x), dtype=float)
        mid_x = x/2
        mid_y = y/2
        s = 10
        for i in range(0,y):
            for j in range(0,x):
                sumfilter_pic2[i][j] = self.sumfilter[i][j] * 255
        Image.fromarray(numpy.uint8(sumfilter_pic2)).save("img/sumfiltr.png")
        sumfiltr_pic = QPixmap('img/sumfiltr.png')
        self.filter.setPixmap(sumfiltr_pic.scaled(self.pic_s, self.pic_s))
        self.filter.setFixedSize(self.pic_s,self.pic_s)    


################################################################################
# MAIN                                                                         #
################################################################################

def main():

    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

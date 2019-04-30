from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('pencere.ui', self)
        
        # self.spinBox.valueChanged.connect(self.update_progress)
        self.btnSetAlarm.clicked.connect(self.kur)
        self.timer = QTimer()
        now = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)

    def kur(self):
        
        
        now = QDateTime.currentDateTime()
        tarih = self.dateTimeEdit.dateTime()
        fark = now.msecsTo(tarih)

        if fark < 1:
            print('eksi deger girdiniz')
            return

        self.btnSetAlarm.setEnabled(False)
        
        print(fark)
        self.timer.timeout.connect(self.tick)
        self.timer.start((fark * 5) / (100))



    def tick(self):
        p_deger = self.progressBar.value()
        self.update_progress(p_deger - 5)

        if p_deger < 1:
            self.timer.stop()
            self.btnSetAlarm.setEnabled(True)
            self.update_progress(100)
        

    def update_progress(self, sayi):
        self.progressBar.setValue(sayi)

app = QApplication(sys.argv)
pen = Pencere()
pen.show()
sys.exit(app.exec_())

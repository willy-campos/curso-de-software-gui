# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:40:15 2021

@author: willy
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class GUI(QMainWindow):
    def __init__(self):
     super().__init__()
     # initialize super class, which creates the Window
     self.initUI()
    def initUI(self):
        self.setWindowTitle('Mi Ventana PyQt5 GUI')
        self.resize(400, 300)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())       

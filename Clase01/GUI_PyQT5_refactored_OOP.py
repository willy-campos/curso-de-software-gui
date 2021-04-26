# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:33:18 2021

@author: willy
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):
    def __init__(self):
     super().__init__()
     # initialize super class, which creates the Window
     self.initUI()
    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())       
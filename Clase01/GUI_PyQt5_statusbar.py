# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:12:13 2021

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
        self.setWindowTitle('PyQt5 GUI')
        self.resize(400, 300)
        self.add_widgets() # <== call new method here
    def add_widgets(self):
        self.statusBar().showMessage('Text in statusbar')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())  


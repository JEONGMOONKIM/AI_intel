import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window=uic.loadUiType('./poster.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_pt.clicked.connect(self.btn_click_slot)
        self.btn_tf.clicked.connect(self.btn_click_slot)
        self.btn_tk.clicked.connect(self.btn_click_slot)
        self.btn_tl.clicked.connect(self.btn_click_slot)

    def btn_click_slot(self):
        btn=self.sender()
        self.lbl_pt.hide()
        self.lbl_tf.hide()
        self.lbl_tk.hide()
        self.lbl_tl.hide()
        if btn.objectName()=='btn_pt':self.lbl_pt.show()
        elif btn.objectName()=='btn_tf':self.lbl_tf.show()
        elif btn.objectName()=='btn_tk':self.lbl_tk.show()
        elif btn.objectName()=='btn_tl':self.lbl_tl.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_())
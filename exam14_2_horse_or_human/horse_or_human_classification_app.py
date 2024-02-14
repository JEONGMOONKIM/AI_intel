import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

form_window = uic.loadUiType('./horse_or_human.ui')[0]

class Exam(QWidget,form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = ('C:/workspacepython-intel2/Intel_AI_S2/datasets/horse-or-human/test02.jpg','')
        self.model = load_model('./horse_or_human_1.0.h5')
        self.btn_open.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):
        old_path=self.path
        self.path = QFileDialog.getOpenFileName(self,'Open file',           #파일 선택
                                                '../datasets/horse-or-human/horse_human',
                                                'Image File(*.jpg;*.png);;''All Files(*.*)')


        print(self.path)

        if self.path[0]=='':
            self.path=old_path
        try:
            pixmap = QPixmap(self.path[0])      #pixmap에 경로를 받는다
            self.lbl_image.setPixmap(pixmap)    #image 출력

            img = Image.open(self.path[0])      #경로
            img = img.convert('RGB')
            img = img.resize((64, 64))
            data = np.asarray(img)
            data = data /255
            data = data.reshape(1,64,64,3)
            pred = self.model.predict(data)
            print(pred)
        except:
            self.lbl_result.setText('손상된 이미지')

        if pred <0.5:
            self.lbl_result.setText('말')
        else:
            self.lbl_result.setText('사람')
        print(self.path)

if __name__ =='__main__':
    app =QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_())
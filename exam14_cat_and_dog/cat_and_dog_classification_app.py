import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model


form_window=uic.loadUiType('./cat_and_dog.ui')[0] #uic:ui 파일을 클래스로 바꿔줌

class Exam(QWidget, form_window): #두 개의 클래스를 상속해 Exam 클래스를 만듬.
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path=('C:/workspacepython-intel2/Intel_AI_S2/datasets/cat_dog/test01.jpg')
        self.model=load_model('./cat_and_dog_0.836.h5')
        self.btn_open.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):
        old_path=self.path
        self.path=QFileDialog.getOpenFileName(self, 'Open file',
                                              '../datasets/cat_dog',
                                              'Image File(*.jpg;*.png);;All Files(*.*)')
        print(self.path)
        if self.path[0]=='':
           self.path=old_path
        try:
            pixmap = QPixmap(self.path[0])
            self.lbl_image.setPixmap(pixmap)

            img = Image.open(self.path[0])
            img = img.convert('RGB')
            img = img.resize((64, 64))
            data = np.asarray(img)
            data = data / 255
            data = data.reshape(1, 64, 64, 3)
            pred = self.model.predict(data)
            print(pred)
        except:
            self.lbl_result.setTxt('손상된 이미지 입니다.')

        if pred<0.5:
            self.lbl_result.setTxt('고양이 입니다.')
        else:
            self.lbl_result.setTxt('강아지 입니다.')

        print(self.path)


    #     self.btn_push.clicked.connect(self.btn_clicked_slot)
    # def btn_clicked_slot(self):
    #     self.label.setText('Hi World!')

if __name__=='__main__': #실행한 파일의 이름이 '__main__'이면 실행. import시 해당 파일이 '__main__'파일이 됨.
    app=QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_()) #윈도우 동작 모니터링 -> 윈도우 종료시 exec_() 리턴 -> exit코드 활성화.
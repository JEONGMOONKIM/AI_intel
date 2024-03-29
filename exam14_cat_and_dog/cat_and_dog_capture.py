import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import time

form_window=uic.loadUiType('./cat_and_dog.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model=load_model('./cat_and_dog_0.836.h5')

        self.btn_open.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):
        capture=cv2.VideoCapture(0) #webcam이 있으면 webcam이 우선(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 64)
        flag=True
        while flag:
            v, frame=capture.read()
            print(type(frame))


            if(v): #캡쳐를 잘 해서 트루일 경우
                cv2.imshow('VideoFrame', frame)
                cv2.imwrite('./capture.png', frame)
            # time.sleep(0.5) #동영상 저장. 0.5: 1초에 2frame
            key=cv2.waitKey(30)
            if key==27: #esc 아스키코드값: 27. while문 빠져나가기
                flag=False

            pixmap=QPixmap('./capture.png')
            self.lbl_image.setPixmap(pixmap)

            try:
                img=Image.open('./capture.png')
                img=img.convert('RGB')
                img=img.resize((64,64))
                data=np.asarray(img)
                data=data/255
                data=data.reshape(1,64,64,3)

                pred=self.model.predict(data)
                print(pred)
                if pred<0.5:
                    self.lbl_result.setText('고양이')
                else:
                    self.lbl_result.setText('강아지')
            except:
                print('error')

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_())




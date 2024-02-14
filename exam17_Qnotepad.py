import  sys #모듈을 임포트
from PyQt5.QtWidgets import * #위젯 클래스를 임포트 다양한 GUI 위젯을 제공
from PyQt5 import uic #디자인한 GUI 레리아웃 파일(ui)을 파이썬 코드로 변환하는 기능 제공

form_window = uic.loadUiType('./Qnotepad.ui')[0]
#디자인한 UI 파일(.ui)을 로드하는 과정

class Exam(QMainWindow, form_window):
#UI 파일에서 생성된 레이아웃과 위젯을 설정하고 액션과 해당 슬롯을 연결하는 과정
    def __init__(self):
        super().__init__() #부모 클래스인 QMainWindow의 생성자 호출
        self.setupUi(self) #UI파일에서 생성된 클래스의 메서드를 호출
        self.path = ('제목 없음', '') #파일 경로를 저장하는 변수 path를 초기화
        self.edited_flag = False
        self.setWindowTitle(self.path[0] + ' - QT note Pad') ##제목 표시줄 표시
        self.plain_te.textChanged.connect(self.text_changed_slot)
        #텍스트가 변경될때 특정 동작을 수행
        self.plain_te.textChanged.connect(self.text_changed_slot)
        # file menu 구현
        self.actionSave_as.triggered.connect(self.action_save_as_slot)
        self.actionSave.triggered.connect(self.action_save_slot)
        self.actionExit.triggered.connect(self.action_exit_slot)
        self.actionOpen.triggered.connect(self.action_open_slot)
        self.actionNew.triggered.connect(self.action_new_slot)

        # edit menu 구현
        self.actionUn_do.triggered.connect(self.plain_te.undo)
        self.actionCut.triggered.connect(self.plain_te.cut)
        self.actionCopy.triggered.connect(self.plain_te.copy)
        self.actionPaste.triggered.connect(self.plain_te.paste)
        self.actionDelete.triggered.connect(self.plain_te.cut)
        self.actionSelect_all.triggered.connect(self.plain_te.selectAll)

        self.actionFont_2.triggered.connect(self.action_font_slot)

        self.actionAbout.triggered.connect(self.action_about_slot)

    def action_about_slot(self):
        QMessageBox.about(self, 'Qt Not Pad',
                          '''만든이 : abc \n\r버전 정보 : 1.0.0''')

    def action_font_slot(self):
        font = QFontDialog.getFont()
        print(font)
        if font[1]:
            self.path_te.setFont(font[0])

    def save_edited(self):
            if self.edited_flag:
                 ans = QMessageBox.question(self, '저장하기', '저장할까요?',
                                   QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                QMessageBox.Yes)
                 if ans == QMessageBox.Yes:
                     if self.action_save_slot():
                         return
                 elif ans == QMessageBox.Cancel:
                     return 1

    def action_new_slot(self):
        if self.save_edited():
            return

        self.plain_te.setPlainText("")


    def action_open_slot(self):
        if self.edited_flag:
            ans = QMessageBox.question(self, '저장하기', '저장할까요?',
                                           QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                           QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                if self.action_save_slot():
                   return
            elif ans == QMessageBox.Cancel:
                return

        old_path = self.path
        self.path = QFileDialog.getOpenFileName(self, 'Open File', '',
                    'Text Files(*.txt);;Python Files(*.py);;All Files(*.*)')
        if self.path[0]:
            with open(self.path[0], 'r') as f:
                str_read = f.read()
            self.plain_te.setPlainText(str_read)
            self.edited_flag = False
            self.plain_te.textChanged.connect(self.text_changed_slot)
            self.setWindowTitle(self.path[0].split('/')[-1] + ' - QT note Pad')
        else :
            self.path = old_path

    def text_changed_slot(self):
        self.edited_flag = True
        self.setWindowTitle('*' + self.path[0].split('/')[-1] + ' - QT note Pad')
        self.plain_te.textChanged.disconnect(self.text_changed_slot)

    def action_exit_slot(self):
        if self.adited_flag:
            ans = QMessageBox.question(self, '저장하기', '저장할까요?',
                                       QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                       QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                if self.action_save_slot():
                    return
            elif ans == QMessageBox.Cancel:
                return 1


    def action_save_slot(self):
        if self.path[0] != '제목 없음':
            with open(self.path[0], 'w') as f:
                f.write(self.plain_te.toPlainText())
                self.edited_flag = False
                self.plain_te.textChanged.connect(self.text_changed_slot)
                self.setWindowTitle(self.path[0].split('/')[-1] + ' - QT note Pad')
        else : return self.action_save_as_slot()


    def action_save_as_slot(self):
        old_path = self.path
        self.path = QFileDialog.getSaveFileName(self,
                'Save file', '', 'Text File(*,txt);;Python Files(*.py);;All Files(*.*)')
        print(self.path)
        if self.path[0]:
            with open(self.path[0], 'w') as f:
                f.write(self.plain_te.toPlainText())
                self.edited_flag = False
                self.plain_te.textChanged.connect(self.text_changed_slot)
                self.setWindowTitle(self.path[0].split('/')[-1] + ' - QT note Pad')
            return 0
        else :
            self.path = old_path
            return 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())
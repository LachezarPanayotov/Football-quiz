import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDesktopWidget, QWidget
import os


class App(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Football quiz'
        self.initUI()

    def initUI(self):
        self.resize(640, 480)
        self.center()
        self.setWindowTitle(self.title)
        button = QPushButton('Logo quiz', self)
        button.setGeometry(245, 120, 150, 40)
        button.clicked.connect(self.on_click1)
        button = QPushButton('Football questions', self)
        button.setGeometry(245, 170, 150, 40)
        button.clicked.connect(self.on_click2)
        button = QPushButton('Scoreboard', self)
        button.setGeometry(245, 220, 150, 40)
        button.clicked.connect(self.on_click3)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_click1(self):
        ex.close()
        os.system('LogoQuiz\\logo_quiz.py')

    def on_click2(self):
        ex.close()
        os.system('football_questions.py')

    def on_click3(self):
        ex.close()
        os.system('scoreboard.TXT')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Football quiz'
        self.left = 60
        self.top = 60
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Logo quiz', self)
        button.move(100, 70)
        button = QPushButton('Football questions',self)
        button.move(100, 100)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
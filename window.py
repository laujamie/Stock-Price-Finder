import sys
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QWidget, QMainWindow, QPushButton

class Window(QMainWindow):

    def __init__(self, x, y, width, height, title, icon=None):
        super(Window, self).__init__()
        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)
        if icon is not None:
            self.setWindowIcon(QIcon(icon))

        self.init_statusbar()
        
        self.home()

    def init_statusbar(self):
        extract_action = QAction('&Quit', self)
        extract_action.setShortcut('Ctrl+W')
        extract_action.setStatusTip('Quit the app')
        extract_action.triggered.connect(QCoreApplication.instance().quit)

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)
        self.show()


def run_gui(x, y, width, height, title, icon=None):
    app = QApplication(sys.argv)
    gui = Window(x, y, width, height, title, icon)
    sys.exit(app.exec_())

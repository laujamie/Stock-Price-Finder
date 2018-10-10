import sys
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QWidget, QPushButton, QMenuBar, QLineEdit
import api_wrapper

class Window(QWidget):

    def __init__(self, x, y, width, height, title, icon=None):
        # Init for window
        super().__init__()
        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)
        if icon is not None:
            self.setWindowIcon(QIcon(icon))

        # Declare textboxes and menubar
        self.menubar = None
        self.api_box = None
        self.stock_box = None

        self.init_menubar()

        self.init_textboxes()
        
        self.home()

    def init_menubar(self):
        self.menubar = QMenuBar(self)
        file_menu = self.menubar.addMenu('&File')
        extract_action = QAction('&Quit', self)
        extract_action.setShortcut('Ctrl+W')
        extract_action.setStatusTip('Quit the app')
        extract_action.triggered.connect(QCoreApplication.instance().quit)
        file_menu.addAction(extract_action)

    def init_textboxes(self):
        self.api_box = QLineEdit(self)
        self.api_box.move(20, self.menubar.geometry().height()+20)
        self.api_box.resize(self.api_box.sizeHint())
        self.stock_box = QLineEdit(self)
        self.stock_box.move(
            20,
            self.menubar.geometry().height()+40+self.api_box.geometry().height()
            )
        self.stock_box.resize(self.stock_box.sizeHint())

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(self.geometry().width()-btn.geometry().width(),
                 self.geometry().height()-btn.geometry().height())
        self.show()


def run_gui(x, y, width, height, title, icon=None):
    app = QApplication(sys.argv)
    gui = Window(x, y, width, height, title, icon)
    sys.exit(app.exec_())

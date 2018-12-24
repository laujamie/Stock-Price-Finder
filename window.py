import sys
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon, QColor, QPainter
from PyQt5.QtWidgets import QAction, QApplication, QWidget, QPushButton, QMenuBar, QLineEdit, QGroupBox, QFormLayout
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
        # Create menubar buttons
        self.menubar = QMenuBar(self)
        file_menu = self.menubar.addMenu('&File')
        extract_action = QAction('&Quit', self)
        extract_action.setShortcut('Ctrl+W')
        extract_action.setStatusTip('Quit the app')
        extract_action.triggered.connect(QCoreApplication.instance().quit)
        file_menu.addAction(extract_action)
        about_menu = self.menubar.addMenu('&Help')
        extract_action = QAction('&About', self)
        about_menu.addAction(extract_action)

    def init_textboxes(self):
        button_layout = QFormLayout()

        api_box = QLineEdit(self)
        api_box.move(20, self.menubar.geometry().height()+20)
        api_box.resize(api_box.sizeHint())
        stock_box = QLineEdit(self)
        stock_box.move(
            20,
            self.menubar.geometry().height()+40+api_box.geometry().height()
            )
        stock_box.resize(stock_box.sizeHint())

        button_layout.addRow("API Key", api_box)
        button_layout.addRow("Stock Ticker", stock_box)

        self.setLayout(button_layout)

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

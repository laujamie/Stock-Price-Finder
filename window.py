import sys
from matplotlib import style
import matplotlib.pyplot as plt
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon, QColor, QPainter
from PyQt5.QtWidgets import QMessageBox, QAction, QApplication, QWidget, QPushButton, QMenuBar, QLineEdit, QFormLayout
import api_wrapper

style.use('ggplot')

class MainWindow(QWidget):

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

        self.resp_data = None

        self.current_grabber = api_wrapper.TimeSeries()

        # Initialize the window elements
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

        self.api_box = QLineEdit(self)
        self.api_box.move(20, self.menubar.geometry().height()+20)
        self.api_box.resize(self.api_box.sizeHint())
        self.stock_box = QLineEdit(self)
        self.stock_box.move(
            20,
            self.menubar.geometry().height()+40+self.api_box.geometry().height()
            )
        self.stock_box.resize(self.stock_box.sizeHint())

        btn = QPushButton('Fetch data', self)
        btn.clicked.connect(self.clicked)

        button_layout.addRow(" ", None)
        button_layout.addRow("API Key", self.api_box)
        button_layout.addRow("Stock Ticker", self.stock_box)
        button_layout.addRow(btn)

        self.setLayout(button_layout)

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(self.geometry().width()-btn.geometry().width(),
                 self.geometry().height()-btn.geometry().height())
        self.show()

    @pyqtSlot()
    def clicked(self):
        """ activates when the fetch data button is clicked.

        todo:
            * elegant way to exclude certain columns in the result df
        """
        self.current_grabber.set_api_key(self.api_box.text())
        try:
            self.resp_data = self.current_grabber.get_daily(self.stock_box.text())

            # Raise an exception if the received data is an error
            if isinstance(self.resp_data, dict):
                for key, val in self.resp_data.items():
                    if 'Error' or 'Information' in key:
                        raise api_wrapper.ResponseError(val)

            # Plot the data if it exists
            self.resp_data = self.resp_data.T
            exclude = ['5. volume']
            self.resp_data.ix[:, self.resp_data.columns.difference(exclude)].plot()
            plt.show()
        except api_wrapper.MissingApiKey:
            button_reply = QMessageBox.warning(self,
                                              'Error',
                                              'No API Key was provided',
                                              QMessageBox.Ok,
                                              QMessageBox.Ok)
            self.resp_data = None  # reset the response data
        except api_wrapper.ResponseError as e:
            button_reply = QMessageBox.warning(self,
                                               'Error',
                                               '{}'.format(e),
                                               QMessageBox.Ok,
                                               QMessageBox.Ok)
            self.resp_data = None  # reset the response data


def run_gui(x, y, width, height, title, icon=None):
    app = QApplication(sys.argv)
    gui = MainWindow(x, y, width, height, title, icon)
    sys.exit(app.exec_())

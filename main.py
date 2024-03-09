import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,QLabel
from PyQt6.QtGui import QPalette, QColor, QPixmap
import PyQt6

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("BIOMET Demo")

        layout1 = QVBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()
        
        logo = QLabel()
        logoPixmap = QPixmap('BIOMETlogo.png').scaled(234,47)
        

        logo.setPixmap(logoPixmap)

        
       
        layout1.addStretch()
        layout1.addWidget(logo)
        layout1.addWidget(QPushButton(text="Scan ID"))
        layout1.addWidget(QPushButton(text="Register ID"))
        layout1.addWidget(QPushButton(text="Exit"))
        layout1.addStretch()
        

       

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.setContentsMargins(25,25,25,25)
window.show()

app.exec()
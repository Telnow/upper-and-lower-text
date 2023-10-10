import resources

from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class Programm_interface(QWidget):
    def interface(self, Form):
        self.setWindowTitle('Перевод текста в верхний или нижний регистр')
        self.resize(500, 500)
        icon = QIcon()
        icon.addFile(':/mainicon/mainicon.ico', QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)

        self.text_field = QTextEdit()
        self.button_uppercase = QPushButton()
        self.button_uppercase.setText('В верхний регистр')
        self.button_lowercase = QPushButton()
        self.button_lowercase.setText('В нижний регистр')

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button_uppercase)
        self.hbox.addWidget(self.button_lowercase)
        self.vbox.addWidget(self.text_field)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

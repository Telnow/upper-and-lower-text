import sys

from logic import Programm_logic
from PySide6.QtWidgets import QApplication


class Programm(Programm_logic):
    def __init__(self):
        super().__init__()
        self.interface(self)
        self.button_uppercase.clicked.connect(self.to_uppercase)
        self.button_lowercase.clicked.connect(self.to_lowercase)


if __name__ == '__main__':
    app = QApplication()
    window = Programm()
    window.show()
    sys.exit(app.exec())
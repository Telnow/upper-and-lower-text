from interface import Programm_interface


class Programm_logic(Programm_interface):

    def to_uppercase(self):
        self.text = self.text_field.toPlainText().upper()
        self.text_field.setText(self.text)

    def to_lowercase(self):
        self.text = self.text_field.toPlainText().lower()
        self.text_field.setText(self.text)
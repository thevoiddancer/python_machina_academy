from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setReadOnly(False)
        layout.addWidget(self.input_field)

        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, i // 4, i % 4)

        eq_btn = QPushButton("=")
        eq_btn.clicked.connect(self.on_click)
        grid.addWidget(eq_btn, 4, 0, 1, 4)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        sender = self.sender().text()
        if sender == "=":
            try:
                result = str(eval(self.input_field.text()))
                self.input_field.setText(result)
            except:
                self.input_field.setText("Error")
        elif sender == "C":
            self.input_field.clear()
        else:
            self.input_field.setText(self.input_field.text() + sender)

app = QApplication(sys.argv)
calc = Calculator()
calc.show()
sys.exit(app.exec_())


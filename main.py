import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from sympy import symbols, diff, integrate

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        button_layout = QVBoxLayout()
        buttons = [
            ("＋", self.addition),
            ("－", self.subtraction),
            ("×", self.multiplication),
            ("÷", self.division),
            ("微分", self.differentiate),
            ("積分", self.integrate)
        ]

        for text, function in buttons:
            button = QPushButton(text)
            button.clicked.connect(function)
            button_layout.addWidget(button)

        self.layout.addLayout(button_layout)

        self.output_label = QLabel()
        self.layout.addWidget(self.output_label)

    def addition(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.output_label.setText(f"Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def subtraction(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.output_label.setText(f"Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def multiplication(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.output_label.setText(f"Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def division(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.output_label.setText(f"Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def differentiate(self):
        expression = self.input_field.text()
        try:
            x = symbols('x')
            result = diff(expression, x)
            self.output_label.setText(f"Differentiation Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def integrate(self):
        expression = self.input_field.text()
        try:
            x = symbols('x')
            result = integrate(expression, x)
            self.output_label.setText(f"Integration Result: {result}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())
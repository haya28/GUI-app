import sys
from PySide6.QtWidgets import QApplication
from app import CalculatorWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())
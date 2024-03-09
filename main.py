import os
import sys

from PyQt5.QtWidgets import QApplication
from calculator.calculator import CalculatorApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator_screen = CalculatorApp()
    calculator_screen.show()
    sys.exit(app.exec_())

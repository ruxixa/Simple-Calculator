from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

import re

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("ui/calculator.ui", self)
        self.setWindowTitle("github.com/ruxixa")

        self.setWindowIcon(QIcon("ui/icon.ico"))

        self.numbers = [num for num in range(10)]
        self.operation_chars = ["+", "-", "*", "/"]

        self.operation_string = ""

        self.button_dict = {
            self.buttonOne: "1",
            self.buttonTwo: "2",
            self.buttonThree: "3",
            self.buttonFour: "4",
            self.buttonFive: "5",
            self.buttonSix: "6",
            self.buttonSeven: "7",
            self.buttonEight: "8",
            self.buttonNine: "9",
            self.buttonZero: "0",
            self.buttonPlus: "+",
            self.buttonMinus: "-",
            self.buttonMultiply: "*",
            self.buttonDivise: "/",
            self.buttonDot: ".",
            self.buttonPercent: "%",
        }

        all_buttons = list(self.button_dict.keys())

        buttons = [button for button in all_buttons]

        for button in buttons: 
            button.clicked.connect(lambda _, b=button: self.find_button_operation(b))

        self.buttonClear.clicked.connect(self.clear_operation)
        self.buttonEqual.clicked.connect(self.calculate)
            
    def find_button_operation(self, button):
        if self.button_dict[button] in self.operation_chars:
            if self.operation_string[len(self.operation_string) - 1] not in self.operation_chars:
                self.operation_string += self.button_dict[button]

        elif not self.operation_string:
            if self.button_dict[button] not in self.operation_chars:
                self.operation_string = self.button_dict[button]

        else:
            self.operation_string += self.button_dict[button]
            
        print(self.operation_string)

    def clear_operation(self):
        self.operation_string = ""
        
        self.operationLabel.setText("0")
        self.resultLabel.setText("0")

    def find_button_operation(self, button):
        current_char = self.button_dict[button]

        self.operation_string += current_char

        self.operationLabel.setText(self.operation_string)

    def calculate(self):
        parts = re.findall(r'[\d.]+|[\+\-\*/]', self.operation_string)

        result = float(parts[0])

        for i in range(1, len(parts), 2):
            operator = parts[i]
            operand = float(parts[i+1])

            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand

        self.resultLabel.setText(str(result))



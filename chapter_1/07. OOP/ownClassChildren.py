from ownClassParent import MathOperations
import math 

class MoreMathOperations(MathOperations):
    def __init__(self, firstNumber, secondNumber, thirdNumber, fourthNumber):

        super().__init__(self, firstNumber, secondNumber)
        self.thirdNumber = thirdNumber
        self.fourthNumber = fourthNumber

    def mean(self):
        meanOfNumber = (self.firstNumber + self.secondNumber + self.thirdNumber + self.fourthNumber) / 4
        return meanOfNumber

    def maximum(self, fifthNumber, sixthNumber):
        self.fifhNumber = fifthNumber
        self.sixthNumber = sixthNumber
        maximumOfNumbers = max(self.firstNumber, self.secondNumber, self.thirdNumber, self.fourthNumber, self.fifhNumber, self.sixthNumber)
        return maximumOfNumbers


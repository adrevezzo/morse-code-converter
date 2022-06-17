from dict import morseDict

class MorseConverter:

    def __init__(self):
        self.conversion = ""

    def convert(self, entry):
        for char in entry:
            self.conversion += morseDict[char] + " "

        return print(self.conversion)
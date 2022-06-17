from converter import MorseConverter

user_entry = str(input("Enter Phrase for conversion: ")).upper()

conv = MorseConverter()
conv.convert(user_entry)


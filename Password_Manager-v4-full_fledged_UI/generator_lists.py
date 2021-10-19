low_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', "i", "j", "k", "l", "m",
                    "n", 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
high_letters = []

for letter in low_letters:
    high_letters.append(letter.upper())

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, value in enumerate(digits):
    digits[index] = str(value)

characters = ["!", "@", ";", '#', '$', '&', '%', "^", "*", '(', ")", '>', '<']

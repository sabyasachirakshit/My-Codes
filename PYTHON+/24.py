# Test wether a passed letter is a vowel or not.

# Program-

letter = input("enter a letter:")
vowel_box = ['A', 'E', 'I', 'O', 'U']
if letter.capitalize() in vowel_box:
    print(f"The letter '{letter}' is a vowel.")
else:
    print(f"The letter '{letter}' is a consonant.")

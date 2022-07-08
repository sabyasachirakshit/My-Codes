"""
todo: In this program, our objective is to develop a python code that enables users to ENCODE a plaintext into morse code or DECODE a morse code into plaintext.
! Note: Morse Code is a method used in telecommunications to encode text characters as a standardized swquences of two different signal durations, called dots and dashes.
? Example of Morse Code Encoding:

                                                Plaintext-> HELLO WORLD!! 
                      Morse Encoded Message-> .... . .-.. .-.. ---   .-- --- .-. .-.. -.. -.-.-- -.-.--
"""


def encode_to_morse(m_dict):
    plaintext = input('Enter PlainText:')
    plaintext = plaintext.upper()
    plain_lst = list(plaintext)

    encoded_morse = []
    for i in plain_lst:
        encoded_morse.append(m_dict[i])
        encoded_morse.append(' ')
    encoded_message = ""
    for i in encoded_morse:
        encoded_message += i
    print('The Encoded Morse Code Message is:\n', encoded_message)


def retrieve_key(dictionary, val):
    for key, value in dictionary.items():
        if value == " ":
            return " "
        elif value == val:
            return key


def decode_from_morse(m_dict):
    morsetext = input('Enter MorseText:')
    morse_lst = morsetext.split(" ")
    plain_lst = []
    for i in morse_lst:
        plain_lst.append(retrieve_key(m_dict, i))
    plain_text = ""
    for i in plain_lst:
        plain_text += i
    print('The Decoded Plain Text Message is:\n', plain_text)


print('~~~~~Morse Encoding Cipher~~~~')
print('1.Encode PlainText into Morse Code')
print('2.Decrypt Morse Code into PlainText')
c = int(input("Enter choice(1-2):"))
morse_dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '&': '.-..',
    "'": '.----.',
    '@': '.--.-',
    ')': '-.--.-',
    '(': '-.--.',
    ':': '---...',
    ',': '--..--',
    '=': '-....-',
    '!': '-.-.--',
    '.': '.-.-.-',
    '-': '-....-',
    '+': '.-.-.',
    '"': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
}
if c == 1:
    encode_to_morse(morse_dictionary)
elif c == 2:
    decode_from_morse(morse_dictionary)
else:
    print('Wrong Choice!!')
input('\nHit Enter to exit.....')

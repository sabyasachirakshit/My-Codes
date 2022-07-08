def encode_morse(plaintext):
    plaintext = plaintext.upper()
    plain_lst = list(plaintext)
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
    encoded_morse = []
    for i in plain_lst:
        encoded_morse.append(morse_dictionary[i])
        encoded_morse.append(' ')
    encoded_message = ""
    for i in encoded_morse:
        encoded_message += i
    return encoded_message


print(encode_morse("EDABIT CHALLENGE"))
print(encode_morse("HELP ME!"))

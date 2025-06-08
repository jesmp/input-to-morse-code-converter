MORSE_CODE= {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # space between words
}


def msg_to_morse(message):
    morse_code_message = []
    for char in message:
        try:
            code = MORSE_CODE[char.upper()]
            morse_code_message.append(code)
        except KeyError as e:
            morse_code_message.append('err')

    return print(' '.join(morse_code_message))


def morse_to_msg(morse):
    message_from_morse = []
    for item in morse:
        try:
            for key, val in MORSE_CODE.items():
                if val == item:
                    message_from_morse.append(key)
        except:
            print("error")

    return print(''.join(message_from_morse).lower())


initiator=input("Type 'm' for string to morse \nType 's' for morse to string\n\n")

if initiator.lower() == 'm':
    msg_to_morse(input("what is your message? "))
elif initiator.lower() == 's':
    morse_to_msg(input("what is your morse code? ").split(" "))
else:
    print("Incorrect value given, Please try again")
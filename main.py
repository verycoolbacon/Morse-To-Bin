MORSE_CODE_DICT = {
    # Letters
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',
    
    # Numbers
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    # above here is made by Gemini

    # below here is made by verycoolbacon
    '-': '-', '.':'.', '_': '-', ',': '.', '/': '/'
}

import sys
repeat = True
# functions
def text_to_morse_func(text_input):
    text_to_morse = []
    for char in text_input:
        if char.upper() in MORSE_CODE_DICT:
            text_to_morse.append(MORSE_CODE_DICT[char.upper()])
        elif char == " ":
            text_to_morse.append("/")
    return " ".join(text_to_morse)

def morse_to_bin_func(morse_input):
    result = []
    key_dash = input("input for dash: ")
    key_dot = input("input for dot: ")
    for _ in morse_input:
        if _ in ("-" , "_"):
            result.append(key_dash)
        elif _ in ("." , ","):
            result.append(key_dot)
        elif _ == " ":
            result.append(" ")
        elif _ == "/":
            result.append("/")
    return "".join(result)

# main script

while repeat == True:
    user_input = input("| a~Z 0~9 only | invalid input will result in blank | input for encoder: ")
    while True:
        mode_input = input("| 1: text>morse | 2: text>morse>morse-bin | 0/Q/q: force quit | input for mode: ")
        if mode_input == "1":
            print(text_to_morse_func(user_input))
            break
        elif mode_input == "2":
            print(morse_to_bin_func(text_to_morse_func(user_input)))
            break
        elif mode_input in ("0","q","Q"):
            break
        else:
            print("invalid input")
    if mode_input in ("0","q","Q"):
        repeat = False
        break
    while True:
        continue_input = str(input("| continue? | 1/yes/YES/y/Y: yes | 0/no/NO/n/N/q/Q: no | input: "))
        if continue_input in ("1","y","yes","Y","YES"):
            break
        elif continue_input in ("0","n","no","N","NO","q","Q"):
            repeat = False
            break
        else:
            print("invalid input")
# this script is made by verycoolbacon

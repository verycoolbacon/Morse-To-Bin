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
    #made by gemini /\
    #made by verycoolbacon \/
    '-': '-', '.':'.', '_': '-', ',': '.', '/': '/'
}

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
    key_dash = input("input for dash:")
    key_dot = input("input for dot:")
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
user_input = input("input: ")
while True:
    mode_input = input("| 1:text>morse>morse_bin | 2: text>morse | choose mode: ")
    if mode_input == "1":
        print(morse_to_bin_func(text_to_morse_func(user_input)))
        break
    elif mode_input == "2":
        print(text_to_morse_func(user_input))
        break
    else:
        print("number too large,too small or invaild")
# this script is made by verycoolbacon

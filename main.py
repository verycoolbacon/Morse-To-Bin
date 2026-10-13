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
# above here is made by Gemini 3.6 Flash
    '-': '-', '.':'.', '_' : '-', ',' : '.', '/' : '/'
}
MORSE_CODE_DECODE_DICT = {
# this dictionary is made by ChatGPT 5.6 Luna
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
# numbers
    '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0',
# smth else
    '_': '-', ',': '.', '/': '/'
}
# below here is made by verycoolbacon

repeat = True
# functions
def text_to_morse_func(user_input):
    output = []
    for char in user_input:
        if char.upper() in MORSE_CODE_DICT:
            output.append(MORSE_CODE_DICT[char.upper()])
        elif char == " ":
            output.append("/")
    return " ".join(output)

def morse_to_bin_func(user_input):
    morse_user_input = text_to_morse_func(user_input)
    result = []
    custom_format_choice = input("Custom dash/dot choice? [y/n] ")
    if custom_format_choice in ("Y","y",""):
        key_dash = input("input for dash: ")
        key_dot = input("input for dot: ")
    else:
        key_dash = "-"
        key_dot = "."
    for _ in morse_user_input:
        if _ in ("-" , "_"):
            result.append(key_dash)
        elif _ in ("." , ","):
            result.append(key_dot)
        elif _ == " ":
            result.append(" ")
        elif _ == "/":
            result.append("/")
    return "".join(result)

def encoder(user_input):
    while True:
        mode_input = input("| 1: text>morse | 2: text>morse>morse-bin | 0/Q/q: force quit | input for mode: ")

        if mode_input == "1":
            print(text_to_morse_func(user_input))
            break

        elif mode_input == "2":
            print(morse_to_bin_func(user_input))
            break

        elif mode_input in ("0", "q", "Q"):
            return "force quit"
        else:
            print("Invalid input")
def decoder(user_input):
# set sample 1 to first char > compare until different > switch both char position > grouping > use morse dictionary to decode > print output
# burtal force function
    OG_input = user_input
# set sample1 to first charater
    sample1 = OG_input[0]
    sample2 = None
    for char in OG_input:
        if sample1 != char:
# set sample2 to different charater
            sample2 = char
            break
# switching both list charaters and also turning them into dash and dots
    BFO1 = []
    BFO2 = []
    for _ in OG_input:
        if _ == sample1:
            BFO1.append(".")
            BFO2.append("-")
        elif _ == sample2:
            BFO1.append("-")
            BFO2.append(".")
        elif _ == " ":
            BFO1.append(" ")
            BFO2.append(" ")
        else:
            BFO1.append("")
            BFO2.append("")
    print(BFO1,BFO2)
    print(sample1,sample2)
# grouping brutal_force_output (BFO)
# turning BFO into brutal_force_output_string (BFOS) also spilting them
    BFOS1 = "".join(BFO1).split(" ")
    BFOS2 = "".join(BFO2).split(" ")
# decoding using BFOS
    output1 = []
    for string in BFOS1:
        if string == "/":
            output1.append("/")
        else:
            output1.append(MORSE_CODE_DECODE_DICT.get(string,"/"))
    output2 = []
    for string in BFOS2:
        if string == "/":
            output2.append("/")
        else:
            output2.append(MORSE_CODE_DECODE_DICT.get(string,"/"))
# resulting and printing
    result1 = "".join(output1)
    result2 = "".join(output2)
    print(f"Result 1: {result1}\nResult 2: {result2}")
# main script
while repeat == True:
# encoder
    encoder_decorder_input = input("""\nInput for encoder or decoder\n"E" for encoder "D" for decoder "0" to quit: """)
    if encoder_decorder_input in ("e","E"):
        user_input = input("| a~Z 0~9 only | invalid input will result in blank | input for encoder: ")
# decoder
    elif encoder_decorder_input in ("d","D"):
        user_input = input("Input for decoder. Only 2 charaters can appear in one string: ")
        decoder(list(user_input))
# quit
    elif encoder_decorder_input in ("0","q","Q"):
        repeat = False
        break
    else:
        print("Invaild input")
# blank input detect
        if user_input == "":
            user_input = input("\nYou inputted nothing, are you sure?\n| a~Z 0~9 only | Type new input here: ")
# force quit detect
        if encoder(user_input) == "force quit":
            break
# repeat function
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

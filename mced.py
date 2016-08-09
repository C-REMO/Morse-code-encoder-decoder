#!/usr/bin/python3

import argparse

AUTHOR, DESCRIPTION='Omer Ramić <@sp_omer>', 'Morse code encoder/decoder v#0.1f'
CODE = {
        #English alphabet
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        #Numbers
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        
        #Extended
        ' ':'/',        '.':'.-.-.-', ',':'--..--',
        ':':'---...',   '?':'..--..', "'":'.----.',
        '-':'-....-',   '/':'-..-.',  '@': '.--.-.',
        '=':'-...-',    '(':'-.--.',  ')':'-.--.-',
        '+':'.-.-.'

        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def to_morse(chars):
    return ' '.join(CODE.get(char.upper()) for char in chars)

def from_morse(strings):
    return ''.join(CODE_REVERSED.get(string) for string in strings.split())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=AUTHOR)
    parser.add_argument('-m', '--message',  dest='message', help='Message to be encoded (\'hi\') or decoded (\'.... ..\').')
    parser.add_argument('-d', '--decode', dest='decode', action='store_true', default=False, help='Decode message from the morse code.')
    args = parser.parse_args()
    try:
        if args.message:
            if args.decode==True:
                print('Morse code: ' + args.message + '\nMessage: ' + from_morse(args.message))
            else:
                print('Message: ' + args.message + '\nMorse code: ' + to_morse(args.message))
        else:
            parser.print_help()
    except:
        print('ERROR: Check your message.')
        pass

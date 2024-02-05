enc_lib = {'a': '*_', 'b': '_***',
           'c': '_*_*', 'd': '_**',
           'e': '*', 'f': '**_*', 'g': '__*',
           'h': '****', 'i': '**', 'j': '*___',
           'k': '_*_', 'l': '*_**', 'm': '__',
           'n': '_*', 'o': '___', 'p': '*__*',
           'q': '__*_', 'r': '*_*', 's': '***',
           't': '_', 'u': '**_', 'v': '***_',
           'w': '*__', 'x': '_**_', 'y': '_*__',
           'z': '__**', '0': '_____', '1': '*____',
           '2': '**___', '3': '***__', '4': '****_',
           '5': '*****', '6': '_****', '7': '__***',
           '8': '___**', '9': '____*',
           ', ':'--..--', '.':'.-.-.-',
           '?':'..--..', '/':'-..-.', '-':'-....-',
           '(':'-.--.', ')':'-.--.-'}
dec_lib = {}
for k,v in enc_lib.items():dec_lib[v] = k

def encrypt(test):
    enc_str = ''
    for letter in test:
        if letter == ' ':
            enc_str += ' '
        else:
            enc_str += enc_lib[letter] + ' '
    return enc_str




def decrypt(enc_str):
    ltr = ''
    dec_str = ''
    enc_str += ' '

    for enc_ltr in enc_str:
        
        if enc_ltr != ' ':
            i = 0
            ltr += enc_ltr
        else:
            i += 1
            if i == 2:
                dec_str += ' '
            else:
                dec_str += list(enc_lib.keys())[list(enc_lib.values()).index(ltr)]
                ltr = ''

    return dec_str


message = input('Enter the text you want to encode in Morse Code: ')
temp = encrypt(message.lower())
print(temp)
print(decrypt(temp))




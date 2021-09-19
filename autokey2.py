ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('enter message:\n')
    key = input('enter your key:\n')
    mode = input('encrypt or decrypt\n')
    if mode == 'encrypt':
       cipher = encryptMessage(message, key)
    elif mode == 'decrypt':
       cipher = decryptMessage(message, key)
    print(cipher)


def encryptMessage (messages, keys):  
    return cipherMessage(messages, keys, 'encrypt')

def decryptMessage(messages, keys):
    return cipherMessage(messages, keys, 'decrypt')

def cipherMessage (messages, keys, mode):
    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        if mode == 'encrypt':
             text += ALPHA.find(key[k_index])
             key += i.upper()  

        elif mode == 'decrypt':
             text -= ALPHA.find(key[k_index])
             key += ALPHA[text]  
        text %= len(ALPHA)
        
        k_index += 1
        
        cipher.append(ALPHA[text])
    return ''.join(cipher)

if __name__ == "__main__":
    main()

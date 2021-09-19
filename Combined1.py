ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('enter message:\n')
    key = input('enter your key:\n')
    mode = input('encrypt or decrypt\n')

    if mode == 'encrypt':
       cipher = encryptMessage(message, key)
       print(cipher)
       key1= generateKey(cipher, key)
       cipher_text = cipherText(cipher,key1)
       print(cipher_text)

    elif mode == 'decrypt':
       key1= generateKey(message, key) 
       cipher = originalText(message, key1)
       print(cipher)
       cipher_text = decryptMessage(cipher, key)
       print(cipher_text)
    
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - 
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
      
def originalText(text, key):
    orig_text = []
    for i in range(len(text)):
        x = (ord(text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

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

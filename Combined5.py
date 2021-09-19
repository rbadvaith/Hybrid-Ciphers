ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('enter message:\n')
    key1= int(input("Enter key 1: "))
    key2= int(input("Enter key 2: "))
    key = [key1, key2]
    key3 = input('enter your key:\n')
    mode = input('encrypt or decrypt\n')

    if mode == 'encrypt':
       message = affine_encrypt(message, key) 
       cipher = encryptMessage(message, key3)
       print(cipher)
       key4= generateKey(cipher, key3)
       cipher_text = cipherText(cipher,key4)
       print(cipher_text)

    elif mode == 'decrypt':
       key4= generateKey(message, key3) 
       cipher = originalText(message, key4)
       print(cipher)
       cipher_text = decryptMessage(cipher, key3)
       cipher_text = affine_decrypt(cipher_text, key)
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
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y  
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
                  + ord('A')) for t in text.upper().replace(' ', '') ])
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
                    % 26) + ord('A')) for c in cipher ])
if __name__ == "__main__":
    main()

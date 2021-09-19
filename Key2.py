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
def main():
    string = input("Enter String: ")
    strings = input("Enter Key: ")
    alpha = ""
    num = ""
    a=2
    b=3
    c=5
    d=6
    special = ""
    for i in range(len(strings)):
        if ( (i > 1 and i != 4 and i < 7 )and (strings[i].isdigit()) ):
            num = num+ strings[i]
        elif((strings[i] >= 'A' and strings[i] <= 'Z') or
             (strings[i] >= 'a' and strings[i] <= 'z')):
            alpha += strings[i]
        else:
            special += strings[i]
 
    keyword=alpha
    K=2
    res = [int(num[idx : idx + K]) for idx in range(0, len(num), K)]
    key = res
    choice = input("Encrypt/Decrypt: ")
    key3 = generateKey(string, keyword)
    if choice == "Encrypt":
       text=affine_encrypt(string, key) 
       cipher_text = cipherText(text,key3)
       print("Ciphertext :", cipher_text)
    elif choice == "Decrypt":   
       text= originalText(string, key3)
       original=affine_decrypt(text, key)
       print("Originaltext :", original)      
if __name__ == "__main__":
    main()

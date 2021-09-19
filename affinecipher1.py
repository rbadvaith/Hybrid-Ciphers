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
    text = input("Enter String: ")
    key1= int(input("Enter key 1: "))
    key2= int(input("Enter key 2: "))
    key = [key1, key2]
    choice = input("Encrypt/Decrypt: ")
    if choice == "Encrypt":          
       affine_encrypted_text = affine_encrypt(text, key)  
       print('Encrypted Text: {}'.format( affine_encrypted_text ))
    elif choice == "Decrypt":  
       print('Decrypted Text: {}'.format( affine_decrypt(text, key) ))  
if __name__ == '__main__':
    main()

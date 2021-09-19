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
    n= int(input("Enter 4 Digit key : "))
    c = 0
    temp = n
    x = []
    no = 0
    while temp != 0:
        temp = temp//10
        c = c+1
    for i in range(c):
        x.append(n%10)
        n = n//10
    x.sort()
    for i in x:
        no = (no*10)+i
    number=str(no)    
    K=2
    res = [int(number[idx : idx + K]) for idx in range(0, len(number), K)]
    key = res
    choice = input("Encrypt/Decrypt: ")
    if choice == "Encrypt":          
       affine_encrypted_text = affine_encrypt(text, key)  
       print('Encrypted Text: {}'.format( affine_encrypted_text ))
    elif choice == "Decrypt":  
       print('Decrypted Text: {}'.format( affine_decrypt(text, key) ))  
if __name__ == '__main__':
    main()

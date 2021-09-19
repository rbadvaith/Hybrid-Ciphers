import numpy as np
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
def encrypt(msg):
    msg = msg.replace(" ", "")
    C = make_key()
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    P = create_matrix_of_integers_from_string(msg)
    msg_len = int(len(msg) / 2)
    encrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        integer = int(row_0 % 26 + 65)
        encrypted_msg += chr(integer)
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def decrypt(encrypted_msg):
    C = make_key()
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    determinant = determinant % 26
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    C_inverse = C
    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
    C[0][1] *= -1
    C[1][0] *= -1
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 26

    P = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2)
    decrypted_msg = ""
    for i in range(msg_len):
        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
        integer = int(column_0 % 26 + 65)
        decrypted_msg += chr(integer)
        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key():
    determinant = 0
    C = None
    while True:
        cipher = input("Input 4 letter cipher: ")
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer

def main():
    msg = input("Message: ")
    key1= input('enter your key:\n')
    cipher = encryptMessage(msg, key1)
    encrypted_msg = encrypt(cipher)
    print(encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg)
    cipher = decryptMessage(decrypted_msg, key1)
    print(cipher)
if __name__ == "__main__":
    main()

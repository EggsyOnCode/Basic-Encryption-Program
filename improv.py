#use vigner cipher,then make three kinds of swaps within cipher text as a secondarly layer of encryption. and ask the user to choose one of the three. 
#remove the spaces and add random hoshposh of phrases towards the end just to elongate the ciphertext, to make it look intimidating
#store the length of actual_cipher text somewhere , to remove the random mess from decryption 

#define two diff types of intial inputs; one for plaintext ( which will be encrypted and hence it'll have a unique len(a)) and a ciphertext (which will be decrypted and the len of plaintext must be inputed by the user)
import random

list_insert = []
strong_encrypt = ''

#########################################################################################################

#########   defining functions: 

def valid_ascii(index):
    if index > 33 and index < 126:
        x = chr(index)
        return x
    else: 
        while index < 33 or index > 126:
            if index > 126 and index < 219: 
                index = 33 + (index - 126)
                
            elif index > 126 and index > 219:
                index = 33 + (index - 219)
                
            elif index < 33 and index >= 0:
                index = 126 - (33-index)
                
            elif index < 33 and index >= -93 and index < 0:
                index = 93 - (abs(index))
                
        x = chr(index) 
        return x

def encrypt(plaintext, rand_string):
    ciphertext = ''
    for i in range(len(plaintext)): 
        index_str = ord(plaintext[i])
        index_pass = ord(ext_pass[i])
        index = index_str + index_pass
        ciph_char = valid_ascii(index)
        ciphertext += ciph_char 
    # print(ciphertext)
    # return ciphertext
    global strong_encrypt
    strong_encrypt += rand_insert(rand_string, insert, ciphertext)
    return strong_encrypt
    
    

def decrypt(strong_encrypt, insert, len_cipher):
    decrypt_text = ''
    cipher_text = strong_encrypt[insert : (insert+len_cipher)]
    for i in range(len(cipher_text)):
        # print(cipher_text)
        index_str = ord(cipher_text[i])
        index_pass = ord(ext_pass[i])
        index = index_str - index_pass
        decrypt_char = valid_ascii(index)
        decrypt_text += decrypt_char
    return decrypt_text 


def rand_insert(str, index, ciphertext):
    return str[0:index] + ciphertext + str[(index+len(ciphertext)): -1]

#####################################################################################################


####### MAIN INPUTS
print("Input the string that is to be operated on: (NO SPACES ALLOWED): ")
a = str(input())

print("Print a strong password; preferably of 6 characters (only valid ASCII characters)")
password = str(input())



###### RANDOM
len_input = len(a)
insert = random.randint(0,(100-len_input))
list_insert.append(insert)

rand_string = ''

# for generating random key to obsfuscate the ciphertext
for i in range(100):
    ran_ascii = random.randint(33,128)
    ran_char = chr(ran_ascii)
    rand_string += ran_char
    


#### PASSWORD
ext_pass = password
i = 0

# to equalize the length of password to the plaintext for vigen ciphering
if len(password) < len(a): 
    while len(ext_pass) != len(a):
        ext_pass += password[i]
        i += 1
        if i == len(password):
            i = 0
            continue
        else: 
            continue
else:
    pass


print("Choose either E for encryption or D for Decryption: ")
choice = str(input())
if choice == "E":
    print("Your ciphertext: ")
    print(encrypt(a, rand_string))
    print("This is the insert number {} This is the length of plaintext which will be asked later {}".format(list_insert[0], len(a)))
elif choice == "D":
    print("Input the index of the insert key")
    input_index = int(input())
    print("Input the original length of plaintext")
    len_cipher = int(input())
    print("Your original plaintext(now decrypted): ")
    print(decrypt(a,input_index, len_cipher))
    
    




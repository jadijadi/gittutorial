# Vigenere cipher
# author: @alirnamvar at GitHub

alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text = input("Enter your text: ")
input_text = input_text.lower()
keyword = input("and your keyword is: ")
keyword = keyword.lower()
situation1 = input("Chose between \"Encryption\" or \"Decryption\": ")


def key_generator(keyword, len_plaintext=0):
    key_ = ''
    cont = True
    while cont:
        for i in keyword:
            key_ = key_ + i
            if len(key_) == len_plaintext:
                cont = False
                break

    return key_


def generate_encrypt_table(alphabet):
    input = []
    for i in alphabet:
        input.append(i)

    output = []
    num1 = 1
    while num1 != 27:
        to_append = []
        for j in input:
            to_append.append(j)

        # print("this is to_append (num1 = {}): {}".format(num1, to_append))
        output.append(to_append)
        pop_val = input.pop(0)
        # print("pop val:", pop_val)
        input.append(pop_val)
        num1 += 1
    return output


def encryption(key_encrypt=None, plain_text=None, encrypt_table=None):
    alphabet_dic = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10,
                        k=11, l=12, m=13, n=14, o=15, p=16, q=17, r=18,
                        s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26)
    ciphertext = []
    index_key = 0
    # key_encrypt[index_key]
    for i in plain_text:
        for j in encrypt_table:
            # print("J:", j)

            if j[0] == i:
                for k, v in alphabet_dic.items():
                    if key_encrypt[index_key] == k:
                        # print("k in", k)
                        v -= 1
                        ciphertext.append(j[v])
                        index_key += 1
                        break
    return ''.join(ciphertext)


def decryption(encrypt_text=None, encrypt_table=None, key_encrypt=None):

    decryption_text = []
    index_key = 0

    key_encrypt = str(key_encrypt)
    for i in encrypt_text:
        for j in encrypt_table:

            if j[0] == key_encrypt[index_key]:
                for con, ele in enumerate(j):
                    if ele == i:
                        decryption_text.append(encrypt_table[0][con])
                index_key += 1
                break

    return ''.join(decryption_text)


main_table = generate_encrypt_table(alphabet)
key = key_generator(keyword=keyword, len_plaintext=len(input_text))


unvalid_input = True
while unvalid_input:

    if situation1.lower() == "encryption" or situation1.lower() == "decryption":
        unvalid_input = False

    else:
        situation1 = input("Unvalid input!\nTry again: ")


if situation1.lower() == "encryption":
    encrypted_text = encryption(key_encrypt=key, plain_text=input_text, encrypt_table=main_table)
    print("Your text: ", input_text, "\nEncrypted text: ", encrypted_text, sep='')

elif situation1.lower() == "decryption":
    decrypted_text = decryption(input_text, main_table, key)
    print("Your text: ", input_text, "\nDecrypted text: ", decrypted_text, sep='')
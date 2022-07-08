"""
todo: In this program, our objective is to encrypt/decrypt a message using caesar cipher.
!Caesar Cipher is basically a substitution cipher where each letter of plaintext is shifted to a fixed postition to get the ciphertext.
?Example: Plaintext -> HelloWorld (key=2), ciphertext -> JgooqYqtnf
"""
print("~~~~Caesar Cipher~~~~\n1.Encryption\n2.Decryption")
choice = int(input('Enter choice(1-2):'))
if choice == 1:
    string = input("Enter Plaintext:")
    lst = list(string)
    key = int(input('Enter Key:'))
    i = 0
    while(i < len(lst)):
        val = ord(lst[i])+key
        if(val > 122):
            val -= 122
            val += 96
        lst[i] = chr(val)
        i += 1
    string = ""
    string = string.join(lst)
    print('Ciphertext:', string)
elif choice == 2:
    string = input("Enter Ciphertext:")
    lst = list(string)
    key = int(input('Enter Key:'))
    i = 0
    while(i < len(lst)):
        val = ord(lst[i])-key
        if(val < 97):
            val += 26
        lst[i] = chr(val)
        i += 1
    string = ""
    string = string.join(lst)
    print('Ciphertext:', string)
print('\nHit Enter to End.......')
input()

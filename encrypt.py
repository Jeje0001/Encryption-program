import random
import string

chars= string.punctuation + string.digits + " " + string.ascii_letters 
chars=list(chars)
key = chars.copy()
random.shuffle(key)

plain_text=input("Enter a message to encrypt")
cipher_text=""

for a in plain_text:
    index=chars.index(a)
    cipher_text+=key[index]

print(f'original text: {plain_text}')
print(f'cipher_text: {cipher_text}')

cipher_text=input("Enter a message to decrypt")
plain_text=""

for a in cipher_text:
    index=key.index(a)
    plain_text+=chars[index]
print(f'cipher_text: {cipher_text}')
print(f'original text: {plain_text}')

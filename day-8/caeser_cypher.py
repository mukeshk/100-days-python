alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_to_encrypt,shift_counter):
    encrypted_str = ''
    for c in text_to_encrypt:
        index_of_char = alphabets.index(c)
        shifted_index = index_of_char+ shift_counter
        if shifted_index > 26:
            shifted_index = shifted_index%26
        encrypted_str+=(alphabets[shifted_index])
    return encrypted_str

def decrypt(text_to_encrypt,shift_counter):
    decrypted_str = ''
    for c in text_to_encrypt:
        index_of_char = alphabets.index(c)
        shifted_index = index_of_char - shift_counter
        if shifted_index < 0:
            shifted_index = 26 + shifted_index
        decrypted_str+=(alphabets[shifted_index])
    return decrypted_str




if direction=='encode':
    print(encrypt(text,shift))
elif direction=='decode':
    print(decrypt(text,shift))
else:
    print('incorrect choice')
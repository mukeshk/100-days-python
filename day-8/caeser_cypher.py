alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(original_text,shift_amount,encode_or_decode):
    modified_text = ''
    if encode_or_decode=='decode':
        shift_amount*=-1

    for c in original_text:
        if c not in original_text:
            modified_text += c
        else:
            shifted_index = alphabets.index(c)+ shift_amount
            shifted_index = shifted_index%len(alphabets)
            modified_text+=(alphabets[shifted_index])
    return modified_text


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction=='encode' or direction == 'decode':
        print(caeser(original_text=text,shift_amount=shift,encode_or_decode=direction))
    else:
        print('incorrect choice')

    restart = input("Type 'yes' if you want to try again. Otherwise type 'no' \n").lower()
    if restart == "no":
        should_continue = False
        print("Good bye")
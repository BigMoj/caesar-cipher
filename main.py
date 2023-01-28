alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_example, shift_amount, directions):
    final_text = ""
    if directions == "decode":
        shift_amount *= -1
    for char in text_example:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += char

    print(f"the {directions}d text is {final_text}")


should_continue = True
while should_continue:
    direction = input("for encrypt type 'encode' and to decrypt type 'decode':\n")
    text = input("please write your text:\n").lower()
    shift = int(input("type the shift number:\n"))

    shift = shift % 25

    caesar(text_example=text, shift_amount=shift, directions=direction)
    restart = input("type 'yes' to continue or type 'no' to exit.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")


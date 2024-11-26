alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type Encode to encrypt and Decode decrypt the text\n").lower()
text = input("Please enter the text\n").lower()
shift = int(input("Type the number by which you want to shift the letter\n"))

def encrypt(original_text ,shift_amount ):
    cipher = ""
    for letters in original_text:
        letter_shift = alphabets.index(letters) + shift_amount
        cipher += alphabets[letter_shift]
    print(f"Here is the coded text '{cipher}'")

def decrypt(original_text, shift_amount):
    decipher = ""
    for letters in original_text:
        letter_shift = alphabets.index(letters) - shift_amount
        decipher += alphabets[letter_shift]
    print(f"The decoded text is '{decipher}'")

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
alpahbet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

option=input("Type encode to encrupt and type decode to decrypt: \n ").lower()
text=input("Type your message: \n ").lower()
shift=int(input("Type your shift number: \n"))

#ENCRYPT
def encrypt (original_text,shift_amount):
    cipher_text=" "

    for letter in original_text:
        shifted_position= alpahbet.index(letter) + shift_amount
#Modulo to divide position by length of alphabet is 26 letter
        shifted_position %=len (alpahbet)
        cipher_text +=alpahbet[shifted_position]

    print(f"Here is encoded result: {cipher_text}")

#DECRYPT
def decrypt(original_text, shift_amount):
    output_text=" "

    for letter in original_text:
        shifted_position= alpahbet.index(letter) - shift_amount
        shifted_position %=len (alpahbet)
        output_text +=alpahbet[shifted_position]

    print(f"Here is decoded result: {output_text}")

#ENCRYPT AND DECRYPT
def caesar(original_text, shift_amount, encode_decode):
    output_text=""
    if encode_decode == "decode":
         shift_amount *= -1
    for letter in original_text:

        if letter not in alpahbet:
            output_text +=letter
            

        shifted_position= alpahbet.index(letter) + shift_amount
        shifted_position %= len(alpahbet)
        output_text += alpahbet[shifted_position]

    print(f"Here is decoded result: {output_text}")

should_cont=True
while should_cont:

encrypt(original_text=text,shift_amount=shift)
decrypt(text,shift)
caesar(text,shift,option)

restart=input("Type yes to continue.Otherwise type no \n").lower()
if restart =="no":
    should_cont=False
    print("BYE")

def caesar_cipher(message,key):
    decrypted_message = ""

    for char in message:
        if char.isupper():
            decrypted_char = chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            decrypted_char = chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char

    return decrypted_message

message = input("Enter the message:")
key = int(input("Enter the key:"))

decrypted_message = caesar_cipher(message,key)

print("Original message:",message)
print("Shift:",key)
print("Encrypted message:",decrypted_message)

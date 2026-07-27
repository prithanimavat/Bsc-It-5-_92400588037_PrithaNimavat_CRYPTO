#generate SHA-512 hash

import hashlib

text = input("enter message to create hash value:")

sha512_hash = hashlib.sha512(text.encode()).hexdigest()

print("SHA512 Hash:",sha512_hash)

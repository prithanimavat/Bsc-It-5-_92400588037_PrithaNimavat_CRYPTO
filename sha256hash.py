#generate SHA-256 hash

import hashlib

text = input("enter message to create hash value:")

sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("SHA256 Hash:",sha256_hash)

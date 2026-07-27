import hashlib

text = input("Enter message to create hash values:")

SHA1_hash = hashlib.sha1(text.encode()).hexdigest()

print("SHA-1 Hash :" , SHA1_hash)

import hashlib
import os

salt=os.urandom(16)
hash=hashlib.pbkdf2_hmac('sha256',b'password',salt,100000)
print(hash)
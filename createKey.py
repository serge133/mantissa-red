import os
from cryptography.fernet import Fernet

keyDirectory = "/media/misha/Mantissa3x/security"

key = Fernet.generate_key()
with open(f'{keyDirectory}/pass.key', 'wb') as filekey:
    filekey.write(key)

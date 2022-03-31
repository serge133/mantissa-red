from cryptography.fernet import Fernet
keyDirectory = "/Users/jesusangelperezsanchez/Desktop"


key = Fernet.generate_key()
with open(f'{keyDirectory}/pass.key', 'wb') as filekey:
    filekey.write(key)
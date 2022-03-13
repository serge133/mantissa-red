import os
from cryptography.fernet import Fernet

def encrypt(filePath, key):
    try:
        fernet = Fernet(key)

        with open(filePath, 'rb') as file:
            original = file.read()

        # ! encrypting File
        encrypted = fernet.encrypt(original)

        # writing the encrypted data
        with open(filePath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        print(f"FAILED: {filePath}!")


def decrypt(filePath, key):
    try:
        fernet = Fernet(key)
        # opening the encrypted file
        with open(filePath, 'rb') as enc_file:
            encrypted = enc_file.read()
  
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        # writing the decrypted data
        with open(filePath, 'wb') as dec_file:
            dec_file.write(decrypted)
    except:
        print(f"FAILED: {filePath}!")

def encryptFiles(directory, key):
    # We want to encrypt the files
    for fileName in os.listdir(directory):
        filePath=f"{directory}/{fileName}"
        if fileName == ".DS_Store" or os.path.isdir(filePath):
            continue
        else: 
            # Encrypting and Decrypting 
            encrypt(filePath, key)
    status = "ENCRYPTED"
    with open(f'{directory}/crypt/crypt.status', 'w') as crypt:
        crypt.write(status)
    print("Encrypted")

def decryptFiles(directory, key):
    # We want to decrypt the files 
    for fileName in os.listdir(directory):
        filePath=f"{directory}/{fileName}"
        if fileName == ".DS_Store" or os.path.isdir(filePath):
            continue
        else: 
            # Encrypting and Decrypting 
            decrypt(filePath, key)
    
    status = "DECRYPTED"
    with open(f'{directory}/crypt/crypt.status', 'w') as crypt:
        crypt.write(status)
    print("Decrypted")





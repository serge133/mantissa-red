import os
from cryptography.fernet import Fernet
from datetime import datetime

keyDirectory = "/Users/jesusangelperezsanchez/Desktop"

# a universal way for python to get path on any operating system, however keyDirectory not work because not every operating system has that path to external drives
home = os.path.expanduser('~')
directory = os.path.join(home, "Desktop", "Secure")
output = []
output.append(f"\t\tLOG: {datetime.now()}\n")
output.append(f"Working directory: {directory}\n")
status = ""

with open(f"{directory}/crypt/crypt.status", 'r') as crypt:
    status = crypt.read()


def encrypt(fileName, key):
    try:
        output.append(f"Encrypting {fileName}...\n")
        fernet = Fernet(key)

        with open(f'{directory}/{fileName}', 'rb') as file:
            original = file.read()

        # ! encrypting File
        encrypted = fernet.encrypt(original)

        # writing the encrypted data
        with open(f'{directory}/{fileName}', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        output.append("\tSuccess\n")
    except:
        output.append("\tFailed!\n")
        print(f"FAILED: {fileName}!")


def decrypt(fileName, key):
    try:
        output.append(f"Decrypting {fileName}...\n")

        fernet = Fernet(key)
        # opening the encrypted file
        with open(f'{directory}/{fileName}', 'rb') as enc_file:
            encrypted = enc_file.read()
  
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        # writing the decrypted data
        with open(f'{directory}/{fileName}', 'wb') as dec_file:
            dec_file.write(decrypted)
        output.append("\tSuccess\n")
    except:
        output.append("\tFailed!\n")
        print(f"FAILED: {fileName}!")

key = None

# * TO CREATE A NEW KEY
# key = Fernet.generate_key()
        # with open(f'{keyDirectory}/pass.key', 'wb') as filekey:
            # filekey.write(key)

# If there is an existing key use it [FETCHES OR CREATES KEY]
try:
    with open(f'{keyDirectory}/pass.key', 'rb') as filekey:
                key = filekey.read()
except: 
    print("Key Not Found!")
    output.append("key not found: aborting...\n")
    with open(f'{directory}/log.txt', 'w') as log:
        log.write(''.join(output))
    exit()

# print(f"[encrypt] or [decrypt]?")
# encOrDec = str(input())

if status == 'DECRYPTED':
    # We want to decrypt the files
    print("encrypting...\n")
    for fileName in os.listdir(directory):
        if fileName == ".DS_Store" or os.path.isdir(f"{directory}/{fileName}"):
            output.append(f"Encrypting {fileName}...\n")
            output.append("\tFailed\n")
            continue
        else: 
            # Encrypting and Decrypting 
            encrypt(fileName, key)
    status = "ENCRYPTED"
    print(status)
else:
    # We want to encrypt the files 
    print("decrypting...\n")
    for fileName in os.listdir(directory):
        if fileName == ".DS_Store" or os.path.isdir(f"{directory}/{fileName}"):
            output.append(f"Decrypting {fileName}...\n")
            # It is a folder
            output.append("\tFailed\n")
            continue
        else: 
            # Encrypting and Decrypting 
            decrypt(fileName, key)
    status = "DECRYPTED"
    print(status)

output.append(f"\n\t\tStatus: {status}\n")
output.append(f"Pass key stored on Mantissa, precisely in {keyDirectory}/pass.key\n\n")
output.append('---------------------------------------------------------------------------------------------\n\n')

with open(f'{directory}/crypt/log.txt', 'r+') as log:
    existingContent = log.read()
    log.seek(0)
    log.write(''.join(output) + existingContent)

with open(f'{directory}/crypt/crypt.status', 'w') as crypt:
    crypt.write(status)

print(f"Done. Log can be found {directory}/crypt/log.txt")
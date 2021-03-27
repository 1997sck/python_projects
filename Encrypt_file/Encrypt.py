# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey: #Open the file that contains the key.
    filekey.write(key)
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key) #Initialize the Fernet object and store it in the fernet variable

    # opening the original file to encrypt
    with open('game.csv', 'rb') as file: #Read the original file.
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original) #Encrypt the file and store it into an object.

    # opening the file in write mode and
    # writing the encrypted data
    with open('game.csv', 'wb') as encrypted_file: #Then write the encrypted data into the same file game.csv.
        encrypted_file.write(encrypted)
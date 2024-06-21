#!/usr/bin/env python3
import json
import sys

from werkzeug.security import check_password_hash, generate_password_hash

passwd_file = "/etc/fileup/passwd"

if len(sys.argv) < 1:
    print("No user supplied")
    sys.exit(1)

user = sys.argv[1]

with open(passwd_file, "r") as p:
    auth = json.load(p)

password = input("Enter password: ")

auth[user] = generate_password_hash(password)


with open(passwd_file, "w") as p:
    json.dump(auth, p)

with open(passwd_file, "r") as p:
    auth_test = json.load(p)

if check_password_hash(auth_test[user], password):
    print("OK")
else:
    print("Failed")
    sys.exit(1)

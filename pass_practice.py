# Goal is to practice usernames and passwords for flight tracker app

import bcrypt


username = input('enter a username: ')
password = input('enter a password: ')

password_bytes = password.encode('utf-8')

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

print(hashed)

users = {}
users[username] = hashed

login_username = input('enter your username: ')
if login_username in users:
    print('username exists')
    login_attempt = input('enter your password again: ')
    login_attempt_bytes = login_attempt.encode('utf-8')
    if bcrypt.checkpw(login_attempt_bytes, users[login_username]):
        print('Password matches!')
    else:
        print('Wrong password')
else:
    print('username does not exist')
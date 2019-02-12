import random

chars = 'acbdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?<>/\|[]{}-_=+:;,.'

x = int(input('How many characters would you like in your password? '))
password = ''
for i in range(x):
    password += random.choice(chars)
print(password)
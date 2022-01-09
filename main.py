import secrets
import string

char_amount = {}

print("How many characters should the password be? (leave blank & press enter for 8 charaters):")
char_amount = input()

char_amount_isnt_empty = bool(char_amount)

if char_amount_isnt_empty == False:
    char_amount = 8

char_amount = int(char_amount)

possible_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(possible_chars) for i in range(char_amount))

print(password)

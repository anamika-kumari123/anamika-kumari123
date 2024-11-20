import re

def validating_password(passwords):
    password = passwords.split(',')

    valid_password = []

    lower_case_letters = re.compile(r'[a-z]')
    upper_case_letters = re.compile(r'[A-Z]')
    digit = re.compile(r'[0-9]')
    special_chars = re.compile(r'[$#@]')

    for i in password:
        if (6 <= len(i) <= 12 and
            lower_case_letters.search(i) and
            upper_case_letters.search(i) and
            digit.search(i) and
            special_chars.search(i)):
            valid_password.append(i)

    return ','.join(valid_password) if valid_password else "No valid passwords found."

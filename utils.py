from random import randint
import re

def random_phone_number():
    number = ''.join(str(randint(0,9)) for _ in range(0,9))
    return number

def extract_redirect( content ):
    regex = r"[\/]free_time_redirect[\.]cgi[\?]u=[a-zA-Z0-9]*&smsOnly=0"
    matches = re.search(regex, content)
    return matches.group(0)


def extract_user_password(content):
    regex = r"username\":\"([a-zA-Z0-9]*)\",\"password\":\"([a-zA-Z0-9]*)\""
    matches = re.search(regex, content)

    user = matches.group(1)
    password = matches.group(2)

    return user, password

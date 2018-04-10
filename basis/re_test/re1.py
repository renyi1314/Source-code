import re

num = "13391931202"


def is_phone_num(num):
    match_mub = re.findall("^1[34578]\d{9}$", num)
    if match_mub:
        return True
    else:
        return False

# def is_email

is_phone_num(num)

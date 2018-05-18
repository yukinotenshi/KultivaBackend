from random import choice
import string
import hashlib
from config import HASH_SALT

def generate_random_string(length=30):
    every_string = string.ascii_letters + string.digits

    result = ""

    for _ in range(length):
        result += choice(every_string)

    return result


def hash_keyword(raw : str):
    m = hashlib.md5()
    m.update(HASH_SALT.encode("utf8"))
    m.update(raw.encode("utf8"))

    return m.hexdigest()

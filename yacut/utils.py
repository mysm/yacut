import random
import string
import re

SHORT_LINK_REGEXP = r"^[a-zA-Z0-9]{1,6}$"


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    short_link = "".join(random.choice(characters) for i in range(6))
    return short_link


def unique_shor_id_correct(short):
    pattern = re.compile(SHORT_LINK_REGEXP)
    return pattern.match(short)

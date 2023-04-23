import random
import string


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    short_link = "".join(random.choice(characters) for i in range(6))
    return short_link

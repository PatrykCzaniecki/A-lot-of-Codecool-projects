import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    small_letters = [random.choice(string.ascii_lowercase) for i in range(number_of_small_letters)]
    capital_letters = [random.choice(string.ascii_uppercase) for i in range(number_of_capital_letters)]
    digits = [random.choice(string.digits) for i in range(number_of_digits)]
    special_chars = [random.choice(allowed_special_chars) for i in range(number_of_special_chars)]
    list_of_id = small_letters + capital_letters + digits + special_chars
    random.shuffle(list_of_id)
    id = ''.join(list_of_id)
    return id
import string
import random

string_with_all_characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password_lenght = int(input("Wprowadź długość hasła "))
password = []

for i in range(password_lenght):
    password.append(random.choice(string_with_all_characters))

print("".join(password)) 
import json
import random
import string

mails = (
    'mail.ru',
    'inbox.ru',
    'list.ru',
    'bk.ru',
    'ya.ru',
    'yandex.com',
    'yandex.ua',
    'yandex.ru',
    'gmail.com',
)


# Get random service
def random_service(list):
    return random.choice(list)


# Creating random name
def random_name():
    with open("modules/jackphone/fullz.json", "r") as names:
        names = json.load(names)["names"]
    return random.choice(names)


# Creating random suffix for emails
# %random_name%SUFFIX@%random_email%
def random_suffix(int_range=4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)


# Create random email by name, suffix, mail
# Example Billy3715@gmail.com
def random_password():
    return random_name() + random_suffix(int_range=10)


# Creating random token
def random_token():
    letters = string.ascii_letters + string.digits
    return "".join(
        random.choice(letters) for _ in range(random.randint(20, 50)))


# Get random user agent
def random_useragent():
    with open("modules/jackphone/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)

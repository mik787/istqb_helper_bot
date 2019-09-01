from glossary import GLOSSARY
import random

d = GLOSSARY


def get_value_by_key(key):
    return d.get(key)


def get_random_item():
    item = random.choice(list(d.items()))
    s = str(item[0].upper() + ': ' + '\n\n' + item[1])
    return s


def search_by_key(key):
    key = key.lower()
    return d.get(key, 'Sorry, nothing found')


def get_keys_list():
    list = []
    for key in d.keys():
        list.append(key)
    return list


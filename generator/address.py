
# -*- coding: utf-8 -*-
from model.address import Address
import random
import string
import os.path
import jsonpickle
import getopt  # чтение опций командной строки
import sys     # для получения опций командной строки

# создание и параметризация генератора задаем количество адресов и имя файла в котором они сохранятся
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["nomber of address", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/addresses.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# создаем генератор который создаст файл jsom в дирректории data
def random_all_symbols(maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " " * 10
    return "".join([random.choice(symbols) for i in range(maxlen)])  # фиксированное количество символов
                                                # range(random.randrange(maxlen))])  # случайное количество
def random_letters(maxlen):
    letters = string.ascii_letters #+ " " * 10
    return "".join([random.choice(letters) for i in range(maxlen)])

def random_digits(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(maxlen)])

random_testdata = [
    Address(first_name=random_letters(10),
            last_name=random_letters(10),
            company=random_all_symbols(7),
            address=random_letters(20),
            zipcode=random_digits(5),
            city=random_all_symbols(10),
            country="США",
            home_phone=random_digits(15),
            mobile_phone=random_digits(15),
            state="Alabama",
            title=random_letters(5))
    for i in range(n)
]

# прописываем путь к файлу относительно conftest, открываем его на записись, прописываем данные
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# прописываем класс для объекта типа адрес для дальнейшего различения объектов разного типа (контакты и тп)
# преобразовываем данные в формат json и записываем их в файл
with open(file, "w") as out:
    jsonpickle.set_encoder_options('simplejson', indent=2)
    out.write(jsonpickle.encode(random_testdata))
# indent разбивает строку на отдельные строки по признаку ключ-значение с двумя отступами
# encode перекодирует .py в .json

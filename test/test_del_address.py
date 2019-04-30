# -*- coding: utf-8 -*-
from random import randrange
from data.addresses import fixed_testdata


def test_delete_some_address(app):
    if app.address.count() == 0:
        app.address.add(fixed_testdata[0])
    old_address_list = app.address .get_address_list()
    index = randrange(len(old_address_list))  # генерация случайного индекса
    app.address.delete_by_index(index)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) - 1 == len(new_address_list)
    old_address_list[index:index+1] = []  # удаляем значение с нужным индексом
    assert old_address_list == new_address_list  # метод __eq__ в model/address производит сравнение по значению



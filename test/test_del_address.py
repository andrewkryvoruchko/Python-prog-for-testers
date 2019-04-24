# -*- coding: utf-8 -*-
from model.address import Address
from random import randrange


def test_delete_some_address(app):
    if app.address.count() == 0:
        app.address.add(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="123456", mobile_phone="123456",
                                          state="Киевская область", title="A"))
    old_address_list = app.address .get_address_list()
    index = randrange(len(old_address_list))  # генерация случайного индекса
    app.address.delete_by_index(index)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) - 1 == len(new_address_list)
    old_address_list[index:index+1] = []  # удаляем значение с нужным индексом
    assert old_address_list == new_address_list  # метод __eq__ в model/address производит сравнение по значению



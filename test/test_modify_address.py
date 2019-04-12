# -*- coding: utf-8 -*-

from model.address import Address
from random import randrange


def test_modify(app):
    if app.address.count() == 0:
        app.address.add_temporary(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="123456", mobile_phone="123456",
                                          state="Киевская область", title="ANDR"))
    old_address_list = app.address.get_address_list()
    index = randrange(len(old_address_list))
    address = Address(first_name="VIKA", address="10Th Avenue")
    address.id = old_address_list[index].id
    address.title = old_address_list[index].title
    app.address.modify_by_index(index, address)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) == len(new_address_list)
    old_address_list[0] = address
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)

'''
def test_modify_street(app):
    old_address_list = app.address.get_address_list()
    address = Address(address="10Th Avenue")
    address.id = old_address_list[0].id
    address.title = old_address_list[0].title
    app.address.modify(address)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) == len(new_address_list)
    old_address_list[0] = address
    print('\n', '* * * old', old_address_list)
    print('* * * new', new_address_list)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)
'''

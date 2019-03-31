# -*- coding: utf-8 -*-
from model.address import Address

# при запусте тестов вначале определяется и запускается фикстура метод app указанный в парамете теста

def test_add_first_address(app): # так же параметер app принимает объект Application из фикстуры
    old_address_list = app.address.get_address_list()
    address = Address(first_name="andreW", last_name="kriv", company="IT", address="Ivana Franka 5/16",
                            zipcode="12345", city="Kyiv", country="Украина", home_phone="123456",
                            mobile_phone="123456", state="Киевская область", title="ANDR")
    app.address.add(address)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) + 1 == len(new_address_list)
    old_address_list.append(address)
    print('\n', '* * * old', old_address_list)
    print(' * * * new', new_address_list)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)
    # сравниваем адреса отсортированные по ключу, функция title указывается в качестве ключа

def test_add_second_address(app):
    old_address_list = app.address.get_address_list()
    address = Address(first_name="andrew", last_name="kriV", company="IT", address="George Washington 20",
                      zipcode="67890", city="Columbus", country="США", home_phone="789123",
                      mobile_phone="789123", state="Alabama", title="MUCHO")
    app.address.add_new(address)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) + 1 == len(new_address_list)
    old_address_list.append(address)
    print('\n', '* * * old', old_address_list)
    print(' * * * new', new_address_list)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)




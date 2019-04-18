# -*- coding: utf-8 -*-
from model.address import Address

# при запусте тестов вначале определяется и запускается фикстура метод app указанный в парамете теста

def test_add_first_address(app): # так же параметер app принимает объект Application из фикстуры
    old_address_list = app.address.get_address_list()
    address = Address(first_name="Andrew", last_name="Kriv", company="IT", address="Ivana Franka 5/16",
                            zipcode="12345", city="Kyiv", country="Украина", home_phone="+(1) 11-111",
                            mobile_phone="+(2) 22-222", state="Киевская область", title="AK")
    app.address.add(address)
    assert len(old_address_list) + 1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list.append(address)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)
    # сравниваем адреса отсортированные по ключу, функция title указывается в качестве ключа

def test_add_second_address(app):
    old_address_list = app.address.get_address_list()
    address = Address(first_name="Piter", last_name="Johnson", company="IT", address="George Washington 20",
                      zipcode="67890", city="Columbus", country="США", home_phone="+(3) 33-333",
                      mobile_phone="+(4) 44-444", state="Alabama", title="PJ")
    app.address.add_new(address)
    assert len(old_address_list) + 1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list.append(address)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)

def test_add_third_address(app):
    old_address_list = app.address.get_address_list()
    address = Address(first_name="John", last_name="Smith", company="IT", address="Linkoln Avenu 15",
                      zipcode="11121", city="Trenton", country="США", home_phone="+(5) 55-555",
                      mobile_phone="+(6) 66-666", state="New Jersey", title="JS")
    app.address.add_new(address)
    assert len(old_address_list) + 1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list.append(address)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)



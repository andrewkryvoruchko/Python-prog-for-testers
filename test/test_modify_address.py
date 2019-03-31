# -*- coding: utf-8 -*-

from model.address import Address

def test_modify_name(app):
    app.address.verify_page_with_addresses()
    old_address_list = app.address.get_address_list()
    address = Address(first_name="VIKA")
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
def test_modify_street(app):
    old_address_list = app.address.get_address_list()
    app.address.modify(Address(address="10Th Avenue"))
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) == len(new_address_list)

'''
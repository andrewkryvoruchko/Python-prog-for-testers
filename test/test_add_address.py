# -*- coding: utf-8 -*-
from model.address import Address
from data.add_address import fixed_testdata as testdata
import pytest


# при запусте тестов вначале определяется и запускается фикстура метод app указанный в параметре теста
@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_address(app, address): # так же параметер app принимает объект Application из фикстуры
    old_address_list = app.address.get_address_list()
    app.address.add(address)
    assert len(old_address_list) + 1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list.append(address)
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)
    # сравниваем адреса отсортированные по ключу, функция title указывается в качестве ключа


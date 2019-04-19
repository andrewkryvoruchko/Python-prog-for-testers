from model.address import Address
import re

def test_phones_on_address_page(app):  # прямая проверка производится обрезка
    if app.address.count() == 0:
        app.address.add_temporary(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="+(1) 23-456", mobile_phone="+(7) 89-456",
                                          state="Киевская область", title="ANDR"))
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert clear(contact_from_address_page.home_phone) == clear(contact_from_edit_page.home_phone)
    assert clear(contact_from_address_page.mobile_phone) == clear(contact_from_edit_page.mobile_phone)

def clear(s):
    return re.sub("[-()+ ]", "", s)

def test_merge_phones_on_address_page(app):  # обратная проверка производится склейка
    if app.address.count() == 0:
        app.address.add_temporary(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="+(1) 23-456", mobile_phone="+(7) 89-456",
                                          state="Киевская область", title="ANDR"))
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert clear(contact_from_address_page.all_phones) == merge_phones(contact_from_edit_page)

def merge_phones(contact):
    return "".join(filter(lambda x: x != "",  # соединяем без всяких символов и отфильтровуем пустые строки
                          map(lambda x: clear(x),  # очищаем от символов
                              filter(lambda x: x is not None,  # отфильтровуем значение None
                                     [contact.home_phone, contact.mobile_phone]))))

#return "".join(map(lambda x: clear(x), [contact.home_phone, contact.mobile_phone]))  # в нашем случае достаточно

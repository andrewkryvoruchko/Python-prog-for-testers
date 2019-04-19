


class Contact:

    def __init__(self, id=None, first_name=None, last_name=None, home_phone=None, mobile_phone=None,
                 all_phones=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.all_phones = all_phones

    def __repr__(self):  # representation выводит на консоль не ссылку на объект а значение (содержимое объекта)
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.home_phone, self.mobile_phone,
                                      self.all_phones)

    def __eq__(self, other):  # функция сравнивает именно по значению, смыслу
        return (self.id is None or other.id is None or self.id == other.id) \
                and self.id == other.id \
                and self.first_name == other.first_name \
                and self.last_name == other.last_name \
                and self.home_phone == other.home_phone \
                and self.mobile_phone == other.mobile_phone \
                and self.all_phones == other.all_phones

    def title(self):  # функция возвращающая ключ используемый для сортировки
        return self.title


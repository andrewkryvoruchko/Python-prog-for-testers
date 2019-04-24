


class Address:

    def __init__(self, first_name=None, last_name=None, company=None, address=None, zipcode=None,
                 city=None, country=None, home_phone=None, mobile_phone=None, state=None, title=None,
                 id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.zipcode = zipcode
        self.city = city
        self.country = country
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.state = state
        if title != None:
            self.title = title.upper()
        else:
            self.title = title
        self.id = id

    def __repr__(self):  # representation выводит на консоль не ссылку на объект а значение (содержимое объекта)
        return "%s:%s:%s" % (self.id, self.first_name, self.title)

    def __eq__(self, other):  # функция сравнивает именно по значению, смыслу
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.title == other.title

    def title(self):  # функция возвращающая ключ используемый для сортировки
        return self.title


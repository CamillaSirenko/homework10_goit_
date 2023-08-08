from collections import UserDict

class Field:
    def __init__(self, name):
        self.name = name
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Name(Field):
    def __init__(self):
        super().__init__('Name')

    def set_value(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().set_value(value)


class Phone(Field):
    def __init__(self):
        super().__init__('Phone')
        self.value = []

    def add_number(self, number):
        self.value.append(number)

    def remove_number(self, number):
        if number in self.value:
            self.value.remove(number)


class Record:
    def __init__(self, name):
        self.name = name
        self.optional_fields = {}

    def add_field(self, field):
        if isinstance(field, Field):
            self.optional_fields[field.name] = field

    def remove_field(self, field_name):
        if field_name in self.optional_fields:
            del self.optional_fields[field_name]

    def edit_field(self, field_name, new_value):
        if field_name in self.optional_fields:
            self.optional_fields[field_name].set_value(new_value)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record


if __name__ == "__main__":
    name = Name()
    name.set_value('Bill')
    phone = Phone()
    phone.add_number('1234567890')
    rec = Record(name)
    rec.add_field(phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert 'Bill' in ab.data
    assert isinstance(ab.data['Bill'], Record)
    assert isinstance(ab.data['Bill'].name, Name)
    assert isinstance(ab.data['Bill'].optional_fields['Phone'], Phone)
    assert ab.data['Bill'].optional_fields['Phone'].value[0] == '1234567890'
    print('All Ok :)')
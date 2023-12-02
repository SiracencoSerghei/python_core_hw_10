from collections import UserDict
from classRecord import Record

class AddressBook(UserDict):  # {Vasea: {name: "Vasea", phone: 1234567890}, Petea:{},...}
    """class AddressBook"""
    def add_record(self, record):
        """add record to address book"""
        if not isinstance(record, Record):
            record = Record(record)
        self.data[record.name.value] = record
    def find(self, name):
        """find record by name"""
        if name in self.data:
            return self.data[name]
        else:
            return None
    def delete(self, name):
        """delete record by name"""
        if name in self.data:
            del self.data[name]
    def get_records(self):
        """return list of records from address book"""
        return list(self.values())
    def __str__(self):
        return '\n'.join([str(r) for r in self.values()])


if __name__ == '__main__':

    print(UserDict)
    record = Record('Sergio')
    record.add_phone('1234567890')
    record2 = Record('Bogdan')
    record2.add_phone('0987654321')
    print(record)
    print(record2)
    book = AddressBook()
    book.add_record(record)
    book.add_record(record2)
    print(book.data['Sergio'])
    print(book.data['Bogdan'])
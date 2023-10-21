"""hw_10"""
# from collections import UserDict
# from field import Field
# from className import Name
# from classPhone import Phone
from classRecord import Record
from classAddressBook import AddressBook
from decorators.input_errors import input_errors
from sanitize_phone_nr import sanitize_phone_number


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"
#  ================================
exit_commands = ("good bye", "close", "exit", ".")
OPERATIONS = {
    "hello": greeting,
    "add": add_contact,
    "change": change_contact,
    "phone": get_phone,
    "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye,
}



book = AddressBook()


def add_contact(name, *phones):
    """add contact to dict"""
    contact = book.find(name)
    if contact is None:
        contact = Record(name)
        book.add_record(contact)
    for phone in phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.isdigit():
            contact.add_phone("phone", sanitized_phone)
        else:
            return f"{RED}Phone {phone} is not valid and not added to {name}{RESET}"

def get_phone(name):
    if name in book.data:
        record = book.data[name]
        return f"{GREEN}{name} was found in your contacts! Phones - {'; '.join(record.get_phones())}{RESET}"
    else:
        return f"{RED}There is no contact with this name!{RESET}"

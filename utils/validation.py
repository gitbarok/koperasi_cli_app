import re

class Validation():
    def validation_register(name, password):
        if not re.match("^[a-z ]*$", name):
            return False
        if not (len(name) >= 4) and (len(password) >= 4):
            return False
        else:
            return True

    def validation_borrow(value: str):
        if not re.match('^[0-9]*$', value):
            return False
        if value == '0' or value[0] == '0' or len(value) <= 4:
            return False
        else:
            return True
        
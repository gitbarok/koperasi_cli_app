import re

class Validation():
    def validation_register(name, password):
        """
        This method for validation registers the user, so the user can not give any inputs that can make this app crash.
        1. for name, only accept alphabet and space only
        2. does not accept name < 4 and password <4 character
        """
        if not re.match("^[a-zA-Z ]*$", name):
            return False
        if (len(name) <= 4) and (len(password) <= 4):
            return False
        else:
            return True

    def validation_borrow(value: str):
        """
        This method for validation borrow, so the user can not give any inputs that can make this app crash.
        1. only accept number
        2. only accept number with length more than 4
        3. does not accept number with leadingh 0
        """
        if not re.match('^[0-9]*$', value):
            return False
        if value == '0' or value[0] == '0' or len(value) <= 4:
            return False
        else:
            return True
        
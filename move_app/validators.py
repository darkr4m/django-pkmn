from django.core.exceptions import ValidationError

import re

def validate_move_name(name):
    error_message = "Improper format"
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"
    good_name = re.match(regex,name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })
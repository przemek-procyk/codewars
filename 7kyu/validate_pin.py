def validate_pin(pin: str):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6) :
        return True
    else:
        return False
    #return true or false

print(validate_pin("122a"))
########################################################################

def validate_pin(pin: str):
    if pin.isdigit() and len(pin) in (4, 6):
        return True
    else:
        return False
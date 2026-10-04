def check_for_float(val):
    # Attempt to convert the value to a float data type
    try:
        return float(val)
    except ValueError:
        # If the input is NaN, return None
        print("Not a number")
        return None


def check_for_integer(val):
    # If the value has decimals, leave the datatype as a float
    # The modulo operator, %, returns the remainder after dividing one value
    # by another
    if (val % 1) > 0:
        return val
    else:
        return int(val)


def validate_input():
    while True:
        val = input("Enter a number: ")
        val = check_for_float(val)

        # If the value is a float, the check if it is an integer
        if isinstance(val, float):
            val = check_for_integer(val)
            return val

        # Otherwise, if the value is not a float (NoneType),iterate again

def check_for_float(val):
    """
    Attempts to convert a value to a float

    :param val: The value to convert to a float
    :return: Returns the value as a float, otherwise None
    """
    # Attempt to convert the value to a float data type
    try:
        return float(val)
    except ValueError:
        # If the input is NaN, return None
        print("Not a number\n")
        return None


def check_for_integer(val):
    """
    Checks whether a numeric value contains a decimal component

    :param val: The numeric value to check
    :return: Returns the value as an integer if it is a whole number, otherwise
    returns the value as a float
    """
    # If the value has decimals, leave the datatype as a float
    # The modulo operator, %, returns the remainder after dividing one value
    # by another
    try:
        if (val % 1) > 0:
            return val
        else:
            return int(val)
    except ValueError:
        return None


def check_for_positive_value(val: int or float):
    """
    Checks whether a value is greater than 0

    :param val: The numeric value to check
    :return: Returns the value if it is greater than 0, otherwise returns None
    """
    # If a value is negative return None
    if val > 0:
        return val
    else:
        print("Input is negative or equal to 0\n")
        return None


def validate_input():
    """
    Prompts the user to enter a valid numeric value

    :return: Returns the entered value as an integer if it is a whole number
    or as a float if it contains a decimal component
    """
    while True:
        val = input("Enter a number: ")
        val = check_for_float(val)

        # If the value is a float, the check if it is an integer
        if isinstance(val, float):
            val = check_for_integer(val)
            return val

        # Otherwise, if the value is not a float (NoneType),iterate again

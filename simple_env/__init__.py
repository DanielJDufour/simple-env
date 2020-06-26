import os

SINGLE_QUOTE = "'"
DOUBLE_QUOTE = '"'

def has(name, debug=False, ignore_warnings=False):
    if debug:
        print("[simple-env] starting has with name: ", name)

    value = os.getenv(name)
    if debug:
        print("[simple-env] unformatted value is ", value)

    if value is None:
        warning = "[simple-env] could not find " + str(name) + "."
        partials = [
            key
            for key in os.environ
            if name in key or (key in name and len(key) / len(name) > 0.25)
        ]
        if partials:
            warning += " Did you mean " + " or ".join(partials) + "?"
        if not ignore_warnings:
            print(warning)
        return

    return value is not None

def trim(value):
    for i in range(2):
        # remove excessive ' quoting
        if value.startswith(SINGLE_QUOTE) and value.endswith(SINGLE_QUOTE):
            value = value.strip(SINGLE_QUOTE)

        # remove excessive " quoting
        if value.startswith(DOUBLE_QUOTE) and value.endswith(DOUBLE_QUOTE):
            value = value.strip(DOUBLE_QUOTE)
    return value

def clean(value):
    if value in [None, "NULL", "null", "Null", "NONE", "none", "None"]:
        return None
    elif value in ["True", "true", "TRUE"]:
        return True
    elif value in ["False", "false", "FALSE"]:
        return False
    elif value.isdigit():
        return int(value)
    else:
        return value

def get(name, debug=False, ignore_warnings=False):
    if debug:
        print("[simple-env] starting get with name: ", name)

    value = os.getenv(name)
    if debug:
        print("[simple-env] unformatted value is ", value)

    if value is None:
        warning = "[simple-env] could not find " + str(name) + "."
        partials = [
            key
            for key in os.environ
            if name in key or (key in name and len(key) / len(name) > 0.25)
        ]
        if partials:
            warning += " Did you mean " + " or ".join(partials) + "?"
        if not ignore_warnings:
            print(warning)
        return

    # remove excessive quoting like value = '"Null"'
    value = trim(value)

    # convert value to appropriate type
    value = clean(value)

    if debug:
        print("[simple-env] finishing get with value:", value)

    return value

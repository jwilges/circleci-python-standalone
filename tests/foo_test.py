import foo


def passthrough_integer_test():
    foo.passthrough(0) == 0
    foo.passthrough(1) == 1


def passthrough_none_test():
    foo.passthrough(None) == None
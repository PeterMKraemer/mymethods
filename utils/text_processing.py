def remove_umlaut(string):
    """
    Removes umlauts from strings and replaces them with the letter+e convention
    :param string: string to remove umlauts from
    :return: unumlauted string
    Code by https://gist.github.com/johnberroa/cd49976220933a2c881e89b69699f2f7
    """
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()
    string = string.encode()
    string = string.replace(u, b'ue')
    string = string.replace(U, b'Ue')
    string = string.replace(a, b'ae')
    string = string.replace(A, b'Ae')
    string = string.replace(o, b'oe')
    string = string.replace(O, b'Oe')
    string = string.replace(ss, b'ss')
    string = string.decode('utf-8')
    return string

def remove_space(string):
    space = ' '.encode()
    string = string.encode()
    string = string.replace(space, b'')
    string = string.decode('utf-8')
    return string

def lowercase(string):
    return string.lower()
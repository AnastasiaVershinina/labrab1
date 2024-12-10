
def decimal_to_hex():
    a = {i: hex(i) for i in range(0, 16)}
    return a
if __name__ == '__main__':
     # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
    print(decimal_to_hex())
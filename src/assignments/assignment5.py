def recursive_decimal_binary(num, bits=7):
    '''
    Given a whole number from the decimal system, converts the number to 8-bit binary
    Given 86 returns 01010110
    :param num:
    :return:
    '''
    power_value = 2 ** bits
    if num == 0 and bits < 0:
        return ''
    elif num < power_value:
        return '0' + recursive_decimal_binary(num,bits-1)
    elif num >= power_value:
        return '1' + recursive_decimal_binary(num-power_value,bits-1)

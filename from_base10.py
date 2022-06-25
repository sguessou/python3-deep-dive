
def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must b')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode the digits')
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    return ''.join([digit_map[d] for d in digits])

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36 ')
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)

    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(314, 2)
print(e)
print(int(e, base=2))

e = rebase_from10(3451, 16)
print(e)
print(int(e, base=16))

e = rebase_from10(-3451, 16)
print(e)
print(int(e, base=16))

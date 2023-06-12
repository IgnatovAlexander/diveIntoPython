num = int(input('Введите число для перевода его в шестнадцатеричную систему: '))
BASE = 16


def convert(number: int, system: int) -> str:
    temp = list()
    base_string = 'abcdef'
    while number > 0:
        rem_division = number % system
        if rem_division > 9:
            base_id = rem_division - 10
            temp.append(base_string[base_id])
        else:
            temp.append(str(number % system))
        number = number // system
    temp.reverse()
    return ''.join(temp)


print(f'Число {num} в шестнадцатеричной системе {hex(num)}')
print(convert(num, BASE))

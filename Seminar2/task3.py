num1 = str(input('Введите первую десятичную дробь вида a/b: '))
num2 = str(input('Введите вторую десятичную дробь вида a/b: '))
num1_list = num1.split("/")
num2_list = num2.split("/")


def nod(x, y):
    if y == 0:
        return x
    else:
        return nod(y, x % y)


def mult(x, y):
    numerator = int(x[0]) * int(y[0])
    denominator = int(x[1]) * int(y[1])
    return numerator, denominator


def summ(x, y):
    numerator = int(x[0]) * int(y[1]) + int(y[0]) * int(x[1])
    denominator = int(x[1]) * int(y[1])
    return numerator, denominator


x1, y1 = mult(num1_list, num2_list)
x2, y2 = summ(num1_list, num2_list)
print(f'Умножение двух дробей равно {int(x1 / nod(x1, y1))} / {int(y1 / nod(x1, y1))}')
print(f'Сумма двух дробей равны {int(x2 / nod(x2, y2))} / {int(y2 / nod(x2, y2))}')

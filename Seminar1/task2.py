def check_prime(a):
    if a > 2:
        for i in range(2, a // 0.5 + 1):
            if a % i == 0:
                return print("Простое число")
                break
    else:
        return print("Составное число")


def check_limit(a):
    if a < 0 or a > 1000:
        print("Число не корректно")
        return False
    else:
        return True


def check(a):
    c = check_limit(a)
    while not c:
        c = enter_number()
    if c:
        check_prime(c)


def enter_number():
    b = int(input("Введите число от 0 до 1000:"))
    return b


check(enter_number())

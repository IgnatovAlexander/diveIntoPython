from random import randint

num = randint(0, 1001)
print(num)


def check(a):
    for i in range(0, 10):
        if a < num:
            return print("Ваше число меньше, чем задумал компьютер")
            check(enter_number())
        elif a > num:
            return print("Ваше число больше, чем задумал компьютер")
            check(enter_number())
        else:
            return print("Вы угадали")
            break


def enter_number():
    b = int(input("Угадайте число от 0 до 1000: "))
    return b


user_number = check(enter_number())


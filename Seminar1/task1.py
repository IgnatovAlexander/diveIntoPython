def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if c ** 2 == a ** 2 + b ** 2:
            print("Прямоугольный тругольник")
        elif c ** 2 < a ** 2 + b ** 2:
            print("Остроугольный тругольник")
        else:
            print("Тупоугольный тругольник")
    else:
        print("Треугольник не существует")


d = float(input("Введите длину стороны a: "))
e = float(input("Введите длину стороны b: "))
f = float(input("Введите длину стороны c: "))

check(d, e, f)

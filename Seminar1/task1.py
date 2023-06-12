def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if a == b == c:
            return "Равностороний"
        elif a == b or a == c or b == c:
            return "Равнобедренный"
        else:
            return "Разносторонний"
    else:
        print("Треугольник не существует")


d = float(input("Введите длину стороны a: "))
e = float(input("Введите длину стороны b: "))
f = float(input("Введите длину стороны c: "))

check(d, e, f)

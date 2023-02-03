def roots(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Дискриминант меньше нуля, действительных корней нет."
    elif d == 0:
        return f"Корень: {-b/(2*a)}"
    else:
        return f"Корни: {(-b + d**0.5)/(2 * a)}, {(-b - d**0.5)/(2 * a)}"


print(roots(1, -5, 3))
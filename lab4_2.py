import math

def func(x):
    y = (x**3 + x) * (x - math.log(abs(x)) - math.sin(x)) + math.sqrt(x**3 + x**3)
    return y

x = float(input("Введіть x: "))

y = func(x)

print("Результат:", y)

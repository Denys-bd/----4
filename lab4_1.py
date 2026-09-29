import math
x = float(input("Введіть x: "))
y = (math.cos(abs(x**3 - 4)) + math.log(abs(x))) / (math.sqrt(x - 8) + x**2 / 3)
print("Результат:", y)
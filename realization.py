import math

x = math.pi / 8

a = abs(math.sin(x))
b = abs(math.cos(3*x))
c = math.acos(2*x*x)
d = math.acos(3*x*x)

result_1 = 3 * a / b 
result_2 = c / d
over_result = result_1 + result_2

print(f"Result 1: {result_1:.5f}")
print(f"Result 2: {result_2:.5f}")
print(f"Overall Result: {over_result:.5f}")
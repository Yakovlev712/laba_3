import math 

first_value = 0.1
second_value = 0.7
step = 0.05

for number in range(int(first_value * 100), int(second_value * 100) + 1, int(step * 100)):
	x = number / 100

	first_part = math.sin(x ** 2) ** 3 / math.cos(x ** 3) ** 2
	second_part = ((3 + x ** 2) / (1 - 2 * x ** 2)) ** (1 / 2)

	final_result = first_part + second_part
	print(f"x = {x:.2f}, final_result = {final_result:.5f}")
# Add another variable to ex33_1.py function arguments that you can pass
# in that lets you change the +1 on line 8 so you can change how much
# it increments by.

numbers = []

def while_loop(max_num, increment, number_list):
	i = 0
	while i < max_num:
		print(f"At the top i is {i}")
		number_list.append(i)
	
		i += increment
		print("Numbers now: ", number_list)
		print(f"At the bottom i is {i}\n")




while_loop(10, 3, numbers)

print("The numbers: ")

for num in numbers:
	print(num)
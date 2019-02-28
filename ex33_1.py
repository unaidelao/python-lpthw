# Convert ex33.py while-loop to a function that you can call, and replace
# 6 in the test (i < 6) with a variable.

numbers = []

def while_loop(max_num, number_list):
	i = 0
	while i < max_num:
		print(f"At the top i is {i}")
		number_list.append(i)
	
		i += 1
		print("Numbers now: ", number_list)
		print(f"At the bottom i is {i}\n")




while_loop(6, numbers)

print("The numbers: ")

for num in numbers:
	print(num)
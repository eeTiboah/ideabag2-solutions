"""Find neon numbers in a given range.
Title: Neon Number
Description:
A number is said to be a Neon Number
if the sum of digits of the square of the number
is equal to the number itself.
Example- 9 is a Neon Number.
9*9=81 and 8+1=9.
Hence it is a Neon Number.
The user is prompted to input a range eg 0-50.
"""


f_num = int(input("Enter lower bound: "))
l_num = int(input("Enter upper bound: "))

for i in range(f_num,l_num+1):
	mult = i**2
	str_mult = str(mult)
	str_sum = 0
	for n in str_mult:
		str_sum+=int(n)
		if str_sum == i:
			print(f"{i} is a neon number")

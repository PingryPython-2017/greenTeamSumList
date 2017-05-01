# Rebecca Lin and Simon Ribeiro
# 5/1/16

def sum_list(numbers):
	""" This program takes in numbers from a list and returns the sum """
	
	sum = 0 
	
	if len(numbers) ==0: 
		return 0
	else: 
		sum += numbers[0] +sum_list(numbers[1:])
		
		return sum
		
####### MAIN PROGRAM BELOW ########
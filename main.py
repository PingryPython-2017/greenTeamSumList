import sumList

numbers = []

add = input("Tell me some numbers: ")

while add != "" :
	numbers.append(int(add))
	add = input("Tell me another number: ")
	
print(sumList.sum_list(numbers))
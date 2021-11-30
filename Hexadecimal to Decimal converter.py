def value(c):
	if c >= "0" and c <= "9":
		return ord(c) - ord("0")
	else:
		return ord(c) - ord("A") + 10

def hexadecimal_to_decimal(str,base):
	length = len(str)
	power = 1 
	number = 0	 

	for i in range(length - 1, -1, -1):
		
		if value(str[i]) >= base:
			print("Invalid Number")
			return -1
		number += value(str[i]) * power
		power = power * base
	return number
	
sample_number = str(input("Enter number: "))
base = 16
print("Decimal equivalent of", sample_number, "in base", base, "is", hexadecimal_to_decimal(sample_number, base))
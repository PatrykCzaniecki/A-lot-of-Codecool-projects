def binary_to_decimal():
    print("Enter Binary Number: ", end="")
    binary = int(input())
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print("Equivalent Decimal Value =", decimal)
 
if __name__ == "__main__":
    binary_to_decimal()
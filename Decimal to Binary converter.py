def decimal_to_binary():
    print("Enter Decimal Number: ", end="")
    decimal_number = int(input())
    list = []
    i = 0
    while decimal_number != 0:
        list.insert(i, decimal_number % 2)
        i = i + 1
        decimal_number = int(decimal_number / 2)

    i = i - 1
    list.reverse()
    print("Equivalent Binary Value =", list) 

if __name__ == "__main__":
    decimal_to_binary()
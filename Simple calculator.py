def simple_calculator():
    while True:
        number_one = ask_for_a_number_one(force_valid_input=False) 
        if not number_one:
            break
        math_sign = ask_for_a_math_sign(force_valid_input=True) 
        number_two = ask_for_a_number_two(force_valid_input=True) 
        result = calculation(number_one, math_sign, number_two)
        if result:
            print(f"Wynik działania to {calculation(number_one, math_sign, number_two)}")  
    pass


def calculation(number_one, math_sign, number_two):
    if not is_number(number_one) or not is_valid_sign(math_sign) or not is_number(number_two):
        return None
    result = None
    if math_sign == "+":
        result = number_one + number_two
    elif math_sign == "-":
        result = number_one - number_two
    elif math_sign == "*":
        result = number_one * number_two
    elif math_sign == "/":
        if number_two != 0:
            result = number_one / number_two
        else: 
            print("Błąd! Nie dzielimy przez zero.")
    return result


def ask_for_a_number_one(force_valid_input):
    while True:
        inp = input("Wprowadź pierwszą liczbę: ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                return None
            print("To nie jest liczba, wprowadź liczbę jeszcze raz: ")


def ask_for_a_math_sign(force_valid_input):
    while True:
        math_sign = input("Wprowadź znak działania (do wyboru: +, -, *, /): ")
        if is_valid_sign(math_sign):
            return math_sign
        else:
            if not force_valid_input:
                return None
            print ("Wybrałeś nieznany znak. Spróbuj jeszcze raz.")


def ask_for_a_number_two(force_valid_input):
    while True:
        inp = input("Wprowadź drugą liczbę: ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                return None
            print("To nie jest liczba, wprowadź liczbę jeszcze raz: ")


def is_valid_sign(math_sign):
    MATH_SIGN = ("+", "-", "*", "/")
    return math_sign in MATH_SIGN


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    simple_calculator()
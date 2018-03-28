def input_number():
    number1 = int(input("Please input number 1: "))
    number2 = int(input("Please input number 2: "))
    result = number1 + number2
    print("The number1 + number2 is :", result)
    return result


if __name__ == "__main__":
    input_number()

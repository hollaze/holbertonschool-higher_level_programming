#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    result = 0
    sign = argv[2]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif sign != "+" and sign != "-" and sign != "*" and sign != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if sign == "+":
        result = add(int(argv[1]), int(argv[3]))

    elif sign == "-":
        result = sub(int(argv[1]), int(argv[3]))

    elif sign == "*":
        result = mul(int(argv[1]), int(argv[3]))

    elif sign == "/":
        result = div(int(argv[1]), int(argv[3]))

    print(argv[1], sign, argv[3], "=", result)

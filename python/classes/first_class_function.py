def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


res = calculate(20, 4, operator=divide)

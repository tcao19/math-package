def add_numbers(num1, num2):
    if isinstance(num1, complex):
        return complex(num1.real + num2.real, num1.imag + num2.imag)
    else:
        try:
            return num1 + num2
        except Exception:
            print("Unable to add values of type ", type(num1).__name__, "and", type(num2).__name__)

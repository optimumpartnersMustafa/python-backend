def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
try:
    num = (int)(input("enter a number "))
    print(factorial_recursive(num))
except ValueError as e:
    print(e)
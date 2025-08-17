def make_multiplier_generator(base_num):
    def multiplier(value):
        if base_num == 0:
            return value * value
        else:
            return value * base_num
    return multiplier

doubler = make_multiplier_generator(2)
tripler = make_multiplier_generator(3)
squarer = make_multiplier_generator(0)

print("--- Testing Multipliers ---")
test_value_doubler = 5
print(f"Doubling {test_value_doubler}: {doubler(test_value_doubler)}")

test_value_tripler = 7
print(f"Tripling {test_value_tripler}: {tripler(test_value_tripler)}")

test_value_squarer = 4
print(f"Squaring {test_value_squarer}: {squarer(test_value_squarer)}")

print("\n--- Testing with Different Values ---")
print(f"Doubling 10: {doubler(10)}")
print(f"Tripling 8: {tripler(8)}")
print(f"Squaring 9: {squarer(9)}")
#-------------------------------------------------------------------------------------------------------------------------------------------
#ex2
from functools import wraps

def call_counter(func):
    """
    Decorator that counts how many times a function is called.
    Stores the count as a function attribute: func.call_count
    """
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0 
    return wrapper


@call_counter
def greet(name):
    return f"Hello, {name}!"

@call_counter
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Said hello to {name}"

@call_counter
def calculate_sum(a, b):
    print(f"Calculating sum of {a} and {b}...")
    return a + b

print("Calling say_hello:")
say_hello("Ali")
say_hello("Basil")
say_hello("Ahamd")

print(f"\n'say_hello' has been called {say_hello.calls} times.")

print("\nCalling calculate_sum:")
result1 = calculate_sum(5, 3)
result2 = calculate_sum(10, 20)
print(f"Result 1: {result1}, Result 2: {result2}")

print(f"\n'calculate_sum' has been called {calculate_sum.calls} times.")

@call_counter
def do_nothing():
    pass

print(f"\n'do_nothing' has been called {do_nothing.calls} times (initial).")
do_nothing()
print(f"'do_nothing' has been called {do_nothing.calls} times (after 1 call).")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#ex3

def positive_number_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("All positional arguments must be positive numbers.")
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(f"Keyword argument '{key}' must be a positive number.")
        return func(*args, **kwargs)
    return wrapper

def call_counter(func):
    func.calls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        func.calls += 1
        return func(*args, **kwargs)
    return wrapper

@call_counter
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Said hello to {name}"

@call_counter
def calculate_sum(a, b):
    print(f"Calculating sum of {a} and {b}...")
    return a + b

@positive_number_validator
def process_data(value1, value2, factor=1):
    print(f"Processing {value1}, {value2} with factor {factor}")
    return value1 * value2 * factor

print("Calling say_hello:")
say_hello("Ali")
say_hello("Basil")
say_hello("ahmad")

print(f"\n'say_hello' has been called {say_hello.calls} times.")

print("\nCalling calculate_sum:")
result1 = calculate_sum(5, 3)
result2 = calculate_sum(10, 20)
print(f"Result 1: {result1}, Result 2: {result2}")

print(f"\n'calculate_sum' has been called {calculate_sum.calls} times.")

print("\nCalling process_data (valid):")
print(f"Result: {process_data(10, 5, factor=2)}")

print("\nCalling process_data (invalid - negative):")
try:
    process_data(10, -5)
except ValueError as e:
    print(e)

print("\nCalling process_data (invalid - zero):")
try:
    process_data(10, 0, factor=3)
except ValueError as e:
    print(e)

@call_counter
def do_nothing():
    pass

print(f"\n'do_nothing' has been called {do_nothing.calls} times (initial).")
do_nothing()
print(f"'do_nothing' has been called {do_nothing.calls} times (after 1 call).")


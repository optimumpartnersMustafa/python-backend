n = int(input("Enter your number to check if it is prime: "))

is_prime = True

if n < 2:
    is_prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(" is a prime number")
else:
    print("is not a prime number")
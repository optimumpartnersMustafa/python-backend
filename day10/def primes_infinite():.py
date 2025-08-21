def primes_infinite():
    """
    A generator function that yields an infinite sequence of prime numbers.
    """
    num = 2  # Start checking for primes from 2
    while True:
        is_prime = True
        # Check for divisibility from 2 up to the square root of num
        # If num is divisible by any number in this range, it's not prime
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num  # Yield the number if it's prime
        num += 1  # Move to the next number to check

# Example usage:
# To print the first 10 prime numbers
print("The first 10 prime numbers:")
prime_gen = primes_infinite()
for _ in range(10):
    print(next(prime_gen))

print("\n---")
# You can continue to get more primes as needed
print("The next 5 prime numbers:")
for _ in range(5):
    print(next(prime_gen))
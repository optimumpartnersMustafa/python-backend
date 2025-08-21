class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            if self.count == 0:
                self.count += 1
                return self.a
            elif self.count == 1:
                self.count += 1
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                self.count += 1
                return self.b
        else:
            raise StopIteration

# Example usage
fib_seq = FibonacciIterator(10)
print(list(fib_seq))
#---------------------------------------------------------------------------------------------------------------------------------------
def alternating_signs(numbers):
    for i, num in enumerate(numbers):
        if i % 2 == 1:
            yield -num
        else:
            yield num

# Example usage
numbers = [1, 2, 3, 4, 5]
signs_gen = alternating_signs(numbers)
print(list(signs_gen))
#--------------------------------------------------------------------------------------------------------------------------------------------
words = ["hello", "world"]
char_to_ascii_dict = {word: {char: ord(char) for char in word} for word in words}

# Example usage
print(char_to_ascii_dict)
#-----------------------------------------------------------------------------------------------------------------------------------------------
input_string = "Programming is fun"
vowels_set = {char.upper() for char in input_string if char.lower() in 'aeiou'}

# Example usage
print(vowels_set)
#-------------------------------------------------------------------------------------------------------------------------------------------------
def primes():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Example usage
prime_gen = primes()
for _ in range(6):
    print(next(prime_gen))
def generate_fibonacci(n):
    if n < 0:
        print("Please enter a non-negative number of terms.")
        return []
    if n == 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]

    for i in range(2, n):
        next_fib = series[i - 1] + series[i - 2]
        series.append(next_fib)

    return series

if __name__ == "__main__":
    while True:
        try:
            num_terms_str = input("Enter the number of Fibonacci terms to generate (or 'q' to quit): ")

            if num_terms_str.lower() == 'q':
                print("Exiting the program. Goodbye!")
                break

            num_terms = int(num_terms_str)

            fibonacci_series = generate_fibonacci(num_terms)

            if fibonacci_series:
                print(f"Fibonacci Series (first {num_terms} terms): {fibonacci_series}")
            elif num_terms == 0:
                print("The series for 0 terms is empty.")

        except ValueError:
            print("Invalid input. Please enter a whole number or 'q' to quit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

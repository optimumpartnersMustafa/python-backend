# Ex 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

if __name__ == "__main__":
    person1 = Person("Ahmad", 30)
    person2 = Person("Ali", 24)
    print(person1.introduce())
    print(person2.introduce())

# Ex 2
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {Dog.species}."

if __name__ == "__main__":
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Lucy", "Labrador")
    print(dog1.describe())
    print(dog2.describe())
    Dog.species = "Canis lupus familiaris" 
    print(dog1.describe()) 

# Ex 3
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else: print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        elif amount <= 0: print("Withdrawal amount must be positive.")
        else: print("Insufficient funds.")
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    account = BankAccount("John Doe")
    account.deposit(100)
    account.withdraw(30)
    account.withdraw(200) 
    print(f"Current balance for {account.account_holder}: ${account.get_balance()}")

# Ex 4
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added.")
    def remove_book(self, isbn):
        initial_len = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        if len(self.books) < initial_len: print(f"Book with ISBN {isbn} removed.")
        else: print(f"Book with ISBN {isbn} not found.")
    def list_books(self):
        if not self.books: return "No books in library."
        return "\n".join([book.display_info() for book in self.books])

if __name__ == "__main__":
    library = Library()
    book1 = Book("Python Basics", "A. Developer", "123")
    book2 = Book("Advanced Python", "B. Coder", "456")
    library.add_book(book1)
    library.add_book(book2)
    print(library.list_books())
    library.remove_book("123")
    print(library.list_books())

# Ex 5
class Car:
    total_cars = 0
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1
    def display_car(self):
        return f"{self.make} {self.model}"
    @staticmethod
    def get_total_cars():
        return Car.total_cars

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry")
    car2 = Car("Honda", "Civic")
    print(f"Car 1: {car1.display_car()}")
    print(f"Total cars created: {Car.get_total_cars()}")
    car3 = Car("Ford", "Focus")
    print(f"Total cars created: {Car.get_total_cars()}")

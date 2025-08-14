import math

# Exercise 1: Banking System
class Account:
    def __init__(self, num, holder, bal=0):
        self._num = num
        self._holder = holder
        self._bal = bal

    def deposit(self, amt):
        self._bal += amt
        print(f"Deposited ${amt:.2f}. New balance: ${self._bal:.2f}")

    def withdraw(self, amt):
        if self._bal < amt:
            print("Insufficient funds.")
            return False
        self._bal -= amt
        print(f"Withdrew ${amt:.2f}. New balance: ${self._bal:.2f}")
        return True

    def __str__(self):
        return f"Acc: {self._num}, Holder: {self._holder}, Bal: ${self._bal:.2f}"

    def __eq__(self, other):
        if not isinstance(other, Account): return NotImplemented
        return self._num == other._num

class SavingsAccount(Account):
    def __init__(self, num, holder, bal=0):
        super().__init__(num, holder, bal)
        self.min_bal = 100

    def withdraw(self, amt):
        if (self._bal - amt) < self.min_bal:
            print(f"Withdrawal denied: Min balance ${self.min_bal:.2f} required.")
            return False
        return super().withdraw(amt)

class CheckingAccount(Account):
    def __init__(self, num, holder, bal=0, limit=0):
        super().__init__(num, holder, bal)
        self.overdraft_limit = limit

    def withdraw(self, amt):
        if (self._bal - amt) < -self.overdraft_limit:
            print(f"Withdrawal denied: Exceeds overdraft limit ${self.overdraft_limit:.2f}.")
            return False
        return super().withdraw(amt)

# Exercise 2: Product System
class Product:
    def __init__(self, pid, name, price, qty):
        self._id = pid
        self._name = name
        self._price = price
        self.quantity = qty

    def apply_discount(self, percent):
        self._price -= self._price * (percent / 100)
        print(f"Discounted. New price: ${self._price:.2f}")

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked. New quantity: {self.quantity}")

    def __add__(self, other):
        if not isinstance(other, Product): return NotImplemented
        if self._id != other._id: raise ValueError("Cannot combine different products.")
        return Product(self._id, self._name, self._price, self.quantity + other.quantity)

    def __call__(self):
        print(f"Summary for {self._name} (ID: {self._id}): Price ${self._price:.2f}, Qty {self.quantity}")

class DigitalProduct(Product):
    def __init__(self, pid, name, price, qty, fsize):
        super().__init__(pid, name, price, qty)
        self.file_size = fsize

    def apply_discount(self, percent):
        if percent > 20: percent = 20
        super().apply_discount(percent)

class PhysicalProduct(Product):
    def __init__(self, pid, name, price, qty, weight):
        super().__init__(pid, name, price, qty)
        self.weight = weight

    def apply_discount(self, percent):
        new_price = self._price - (self._price * (percent / 100))
        if new_price < 5:
            percent = ((self._price - 5) / self._price) * 100
            print("Discount adjusted to keep price >= $5.")
        super().apply_discount(percent)

# Exercise 3: University System
class Person:
    def __init__(self, pid, name, email):
        self._id = pid
        self._name = name
        self._email = email

    def display_info(self):
        print(f"ID: {self._id}, Name: {self._name}, Email: {self._email}")

    def get_email(self):
        return self._email

    def __str__(self):
        return f"Person: {self._name}"

    def __repr__(self):
        return f"Person(id='{self._id}', name='{self._name}', email='{self._email}')"

class Student(Person):
    def __init__(self, pid, name, email, major, gpa):
        super().__init__(pid, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self._name} enrolled in {course}.")

    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}, GPA: {self.gpa}, Courses: {', '.join(self.courses)}")

    def __lt__(self, other):
        if not isinstance(other, Student): return NotImplemented
        return self.gpa < other.gpa

    def __repr__(self):
        return f"Student(id='{self._id}', name='{self._name}', email='{self._email}', major='{self.major}', gpa={self.gpa})"

class Professor(Person):
    def __init__(self, pid, name, email, dept):
        super().__init__(pid, name, email)
        self.department = dept
        self.teaching = []

    def assign_course(self, course):
        self.teaching.append(course)
        print(f"Prof. {self._name} assigned to {course}.")

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}, Teaching: {', '.join(self.teaching)}")

    def __repr__(self):
        return f"Professor(id='{self._id}', name='{self._name}', email='{self._email}', department='{self.department}')"


if __name__ == "__main__":
    print("--- Exercise 1: Banking System Demo ---")
    s_acc = SavingsAccount("101", "Ali", 500)
    c_acc = CheckingAccount("201", "Basil", 300, 200)

    s_acc.deposit(100)
    s_acc.withdraw(450)
    s_acc.withdraw(100)

    c_acc.deposit(50)
    c_acc.withdraw(500)
    c_acc.withdraw(100)

    print("\nAccount Info:")
    for acc in [s_acc, c_acc]:
        print(acc)

    print("\n--- Exercise 2: Product System Demo ---")
    d_prod = DigitalProduct("D001", "E-Book", 20.0, 50, 10.5)
    p_prod = PhysicalProduct("P001", "Chair", 100.0, 10, 5.0)

    d_prod.apply_discount(30)
    p_prod.apply_discount(98)

    d_prod.restock(20)

    d_prod2 = DigitalProduct("D001", "E-Book", 20.0, 30, 10.5)
    combined_d_prod = d_prod + d_prod2
    print(f"Combined E-Book quantity: {combined_d_prod.quantity}")

    d_prod()
    p_prod()

    print("\n--- Exercise 3: University System Demo ---")
    s1 = Student("S001", "omar", "omar@uni.edu", "CS", 3.9)
    s2 = Student("S002", "ali", "ali@uni.edu", "Physics", 3.7)
    p1 = Professor("P001", "Dr. ahmad", "ahmad@uni.edu", "Math")

    s1.enroll("Algorithms")
    p1.assign_course("Calculus")

    print("\nDisplay Info:")
    s1.display_info()
    p1.display_info()

    print(f"\n omar < ali (GPA)? {s1 < s2}")
    print(repr(s1))
    print(repr(p1))

# Write programs to illustrate the use of function calls with arguments and functions returning values.

def greet(name):
    print("Hello,", name)

def add(a, b):
    return a + b

greet("Alice")
greet("Bob")

result = add(5, 3)
print("Sum:", result)

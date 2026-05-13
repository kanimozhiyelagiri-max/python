#the + operator is often used to add together two values
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
#using different arithmetic operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#Division always returns a float
x = 12
y = 5

print(x / y)
#Floor division always returns an integer
x = 12
y = 5

print(x // y)
#The count variable is assigned in the if statement
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
#Comparison operators return True or False based on the comparison:

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#chain comparison operators
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
#logical operators are used to combine conditional statements
x = 5

print(x > 0 and x < 10)
#identity operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#membership operators also work with strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
print(6 & 3)
#Parentheses has the highest precedence
print((6 + 3) - (6 + 3))
#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)
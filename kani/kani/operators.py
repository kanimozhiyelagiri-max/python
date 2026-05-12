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

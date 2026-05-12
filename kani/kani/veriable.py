#create a veriable
x = 5
y = "John"
print(x)
print(y)

#specify the data type of a variable, this can be done with casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#using single or double quotes:
x = "John"
# is the same as
x = 'John'

#case sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Each word, except the first, starts with a capital letter(camel case):
myVariableName = "John"

#Each word starts with a capital letter(pascal case)
MyVariableName = "John"

#Each word is separated by an underscore character(snake case)
my_variable_name = "John"

# assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

#collection of values in a list, tuple
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Create a variable outside of a function, and use it inside the function(global variable)
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#the global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





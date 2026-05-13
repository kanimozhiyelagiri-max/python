#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#What is the data type of a list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#The search will start at index 2 (included) and end at index 5 (not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

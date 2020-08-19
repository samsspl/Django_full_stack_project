
a = 5
print(a) 

a += a 
print(a)

# this is a comment in python

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print("my tax ",my_taxes)

#strings

mystring = 'abcdefg'
print(mystring)
print(mystring[-1]) #last index in string (g)
print(mystring[2:]) #slicing the string, prints out from 2 onwards (cdefg)
print(mystring[:3]) #slicing the string, print out up 2 but not including 3 (abc)
print(mystring[2:5]) #slicing the string, print out from 2 up to 4 but not including 5 (cde)

print(mystring[::2]) #step size 2 (aceg)
print(mystring[::3]) #step size 3 (adg)

x = mystring.upper() 
print(x)
x = mystring.lower()
print(x)
x = mystring.capitalize() #only the first letter (Abcdefg)
print(x)
mystring = 'Hello world'
x = mystring.split() # split hello and world ['hello', 'world'] by default it will split at white space
print(x)
x = mystring.split('e') # split into ['H','llo world']
print(x)

# print formatting strings .format method
y = "Insert another string here: {}".format("INSERT ME!")
print(y)
y = "Item one: {} Item two: {}".format("dog" , "cat")
print(y)
y = "Item one: {x} Item two: {y}".format(y = "dog" , x = "cat")
print(y)

#Lists

mylist = [1,2,3,4,5] # 5 items
mylist1 = ['stringhere', 1,2,3,4,5,True,'asef',[1,2,3,4,5]] # 9 items
print(len(mylist))
print(len(mylist1))
print(mylist1[0]) # will print out 'stringhere'
print(mylist1[3]) # will print out 3
print(mylist1[2:]) # will print out from 2 to then end of the list --> ([2,3,4,5,True,'asef',[1,2,3,4,5]])

#adding to the list, unlike string, list are mutable
print('before reassignment:')
print(mylist)
mylist[0] = 'New Item'
print('after reassignment:')
print(mylist)
# mylist.append(["Not New Item","Old Item"]) # will always add to the back of the list but append will not extend the previous list when adding a new lists
# print(mylist)
mylist.extend(["Not New Item", "Old Item"]) # extend will add new list into existing list as continuous list
print(mylist)
item = mylist.pop() # you can also specify the index to pop.
print(item)
print(mylist)
mylist.reverse() # reversed the list
print(mylist)

# new list 
mylists = [3,2,5,67,34,5,65,7,45,8,456,2,9]
mylists.sort() # check the python document for mixed data type sorting
print(mylists)

#Nested list with
newlist = [1,2,3,['x','y','z']]
print(newlist[2]) #print out index 2 which is (3)
print(newlist[3]) #print out index 3 which is a list (['x','y','z'])
print(newlist[3][1]) #print out index 1 (y) of the nested list (['x','y','z']) indexed (3) in newlist

#matrix (list comprehension) *important*
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][0]) # printing out index 0 of list[4,5,6] which is nested inside matrix index 1 

first_col = [row[0] for row in matrix] # printing out every 0 index of nested list inside  matrix

print(first_col)
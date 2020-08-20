def my_function(param1='default'):
    """
    This is the DOCstring
    line 1
    line 2
    line 3
    """
    print("my first python function: {}".format(param1))

my_function()

def hello():
    return "hello"


x = hello()
print(x)

def addNum(num1,num2):
    if type(num1)==type(num2)==type(12):
        return num1+num2
    else:
        return "sorry, I need integers"
resu = addNum(2,5)
# resu = addNum("2","5") # this return '25' in string which is not the function suppose to return
print(resu)

#lambda Expression

#Filter

mylist = [1,2,3,4,5,6,7,8,9]

# def even_bool(num):
#     return num%2 == 0

# evens = filter(even_bool,mylist)
# print(list(evens))

#lambda

# lambda num:num % 2 == 0

evens = filter(lambda num:num % 2 == 0,mylist)
print(list(evens))

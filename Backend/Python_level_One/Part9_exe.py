#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
  for i in range(len(nums)-2):
    print(i)
    if(num[i] == 1 and num[i+1] == 2 and num[i+2] == 3):
      return True
  
  return False
    # CODE GOES HERE
num = [1,2,3,4,5]
print(arrayCheck(num))
num = [1,3,1,2,3]
print(arrayCheck(num))
num = [1,4,4,1,2]
print(arrayCheck(num))
num = [5,1,2,3,5]
print(arrayCheck(num))
num = [5,1,4,3,5,3,1,2,5]
print(arrayCheck(num))
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  res = ""

  for i in range(len(str)):
    if i%2 == 0:
      res = res + str[i]

  return res
  # CODE GOES HERE

print(stringBits('Heeololeo'))
print(stringBits('hello'))
print(stringBits('Weeolcclommoe'))

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  low_a = a.lower() # standardize to lower case 
  low_b = b.lower() # standardize to lower case
  # print(len(low_a), len(low_b))
  # print(low_b[::-1])
  # print(low_a[len(a)-1:(len(a)-len(b)-1):-1])
  if((len(low_a) > len(low_b)) and (low_a[len(a)-1:(len(a)-len(b)-1):-1] == low_b[::-1])):
      return True
  elif ((len(low_a) < len(low_b)) and (low_a[::-1] == low_b[len(b)-1:(len(b)-len(a)-1):-1])):
      return True
  else:
    if(low_a[::-1] == low_b[::-1]): # equal length strings
      return True

  return False




  # CODE GOES HERE
print(end_other('kfc','kfc'))
print(end_other('HiAbc','ABc'))
print(end_other('kfcbc','ABC'))
print(end_other('abC','HeloAbc'))
print(end_other('AC','abPopaBc'))
print(end_other('kfc','PopkFC'))
print(end_other('kfc','Popeye'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  str_ = ''
  for char in str:
    str_ += char + char
  return str_
  # CODE GOES HERE

print('Everything double char:',doubleChar('ABC'))
print('Everything double char:',doubleChar('Hi'))
print('Everything double char:',doubleChar('AABBcc'))
print('Everything double char:',doubleChar('Hi-There'))
print('Everything double char:',doubleChar('welcome'))

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().)
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  total_sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
  return total_sum
  # CODE GOES HERE
def fix_teen(n):
  return n if(n < 13 or n > 19 or n == 15 or n == 16) else 0  # shorthand method
#   # if(n < 13 or n > 19 or n == 15 or n == 16): 
#   #   return n
#   # else: 
#   #   return 0
#   # CODE GOES HERE


print('sum of No teen age:',no_teen_sum(1,2,13))
print('sum of No teen age:',no_teen_sum(1,5,14))
print('sum of No teen age:',no_teen_sum(6,2,17))
print('sum of No teen age:',no_teen_sum(16,12,19))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
  x = 0
  for i in nums:
    if((i % 2) == 0):
      x = x + 1

  return x



b = [2,1,3,2,4,5,6]
print("Numbers of evens in the list:",count_evens(b))

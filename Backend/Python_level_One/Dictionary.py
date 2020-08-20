#dictionaries

my_stuff = {'key0':'abc','key1':"value1", "key2":{'123':[3,'grabme',1]}, "key3":12}
print(my_stuff) #printing out all the key and value pairs
print(my_stuff['key2'])# printing out respective key and value pairs (321)
print(my_stuff['key2']['123'][1].upper()) #nested pairs 

your_stuff = {'lunch':'pizza','bfast':'eggs'}
your_stuff['lunch'] = 'burger'
print(your_stuff['lunch'].capitalize()) # this will make changes permenately
your_stuff['dinner'] = 'pasta' #adding into dictionaries
print(your_stuff)

#Tuples , sets 
#tuples are immutable unlike lists
t = (1,2,3,4,5)
print(t[2])

t = ('a', True, 123)
print(t)

#sets are unordered 

x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.3)
x.add(4)
print(x)  # even though 0.3 was added last but it appears at the beginning of the set ** and No Duplicates **

converted = set([1,1,1,1,2,2,2,3,3,4,4,4,5,5,])
print(converted) #result {1,2,3,4,5} duplicates not included.

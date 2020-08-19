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

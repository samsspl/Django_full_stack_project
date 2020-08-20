if 1<2:
    print('first block')
    if 20<3:
        print('second block')
    # code below this comment will only run line 1 if is true. that include the whole py script
    if 1 > 2:
        print("hello")
    elif  3 == 3:
            print('elif ran')
    else:
        print('last')



seq = [1,2,3,4,5,6,7,8,9]

for item in seq:
    print(item)

d = {"sam":1,'Frank':2,"Dan":3}

for name in d:
    print(name)#printing out keys ('sam','Frank','Dan')
    # print(d[name]) #printing out values 1, 2, 3


mypairs = [(1,2),(3,4),(5,6),(7,8),]

for (tup1,tup2) in mypairs:
    print(tup2) #second item in (,)
    print(tup1) #first item in (,)

i = 1

while i < 5:
    print("i is: {}".format(i))
    i = i + 1


print(list(range(0,5)))

print(list(range(0,20,2))) #this will print from 0 to 20 excluding but in step size 2. [0,2,4,6,8,10,12,14,16,18]

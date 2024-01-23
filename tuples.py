#tuples are immutable , ordered , contains duplicate elements 
#same as list except immutable

myTuple = ("string",4,4.5,True)
myTuple_size = len(myTuple)
item = myTuple[0]
item = myTuple[-1]
for ele in myTuple:
    print(ele)
#insert,remove,append don't work
#slicing same as lists
range_ij = myTuple[1:2]

myTuple2 = ("string2",2,3,4,)
myTuple3 = myTuple + myTuple2
print(myTuple3)

tuple_wparentheses = "string",1,2,"tom" #is a tuple

string,unit1,unit2,tom = tuple_wparentheses
print(unit1,tom)

tuple3 = (1,2,3,3,4,4,5,56)
i1 , *i2 , i3 = tuple3
print(i2)

try:
    print(tuple3[100])
except IndexError: print("index out of bound")
#lists are mutable , ordered , contains duplicate elements , contains elements of different types
myList = ["string",4,4.5,True]
myList2 = list()
# print(myList,myList2)

# print(len(myList))
# print(myList[0])
# print(myList[-1])

# for ele in myList:
#     print(str(ele)+" ")

# if "string" in myList:
#     print("present")
# else: print("absent")

#append,insert
myList2.insert(1,"element2")
print(myList2,len(myList2))
myList2.append("newElements")
myList2.insert(0,"element1")
#print(myList2)

#remove
lastitem = myList2.pop() #remoce and return last item
myList2.remove("element1")
myList2.clear()
myList2.reverse()
#print(myList2)

#sort in-place
myList3 = [1,2,3,4,5]
myList3.sort(reverse=True)
#print(myList3)

#other list
templist = [1,2,3,4,5]
myList4 = sorted(templist,reverse=True)
#print(myList4,templist)

#list concatenation
myList5 = [0]*5
myList6 = [7,8,9,10]
myList7 = myList5+myList6
#print(myList7)

#slicing last index is exclusive
sliced = myList7[2:4] #index 2,3
sliced = myList7[:] #whole list7
sliced = myList7[1:] #start from idx 1
sliced = myList7[:5] #end at idx 5

#stepping in slicing
#mylist7 = [0,0,0,0,0,7,8,9,10]
sliced = myList7[1:8:2] #idx 0,2,4,...
sliced = myList7[::-1] #reverses a list
print(sliced)
list1 = [1,2,3,4]
list2 = list1 #same reference not copy
list2.append(5) #will modify both

list3 = list1.copy() #is a copy

#copy with our own function
list4 = [i*i*i for i in list1] #cube of all in list1

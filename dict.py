#dict is a key-value data structure , unordered , mutable
mydict = {
    "firstName":"pranshu",
    "lastName":"nayak",
    "age":21,
    "sex":"male"
}
mydict5 = dict(name="pranshu",sex="male")
print(mydict5)

# print(mydict)

for keys in mydict:
    print(keys)
keys = mydict.keys()
values = mydict.values()
items = mydict.items()
#print(keys,type(keys),values,type(values),items,type(items))

# for key,value in mydict.items():
#     print(key,value)

#access a key value
try:
    print(mydict["pranshu"])
except KeyError: print("error")

#print(mydict["pranshu"])

#copy a dict
mydict2 = mydict #is a reference not a copy
mydict3 = mydict.copy()
mydict4 = dict(mydict)

#find a key
if "lastName" in mydict:
    print(mydict["lastName"])
else: print("key not present")

#mutability
mydict["lastName"] = "naik"
print(mydict)

mydict["org"] = "oracle"
print(mydict)

del mydict["lastName"]
print(mydict)

#update a given dict with the other
mydict5.update(mydict)
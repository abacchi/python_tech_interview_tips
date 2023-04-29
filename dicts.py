# Also known as hashmap, but really dict

mymap={}
mymap["alice"]=99
mymap["bob"]=92

print(mymap)

# Can update items:
mymap["alice"]=8
print(mymap["alice"])



mymap.pop("alice")
print(mymap)
# Is alice still with us?
print("alice" in mymap)


mymap={"aaron": 99, "bob": 88, "tom": 100}

for key in mymap:
    print(key, mymap[key])

for val in mymap.values():
    print(val)

for key,val in mymap.items():
    print(key, val)
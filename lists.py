# Lists
arr = [1, 2, 3]
print(arr)


arr.append(5)
arr.append(66)
print(arr)

arr.pop()
print(arr)

# Takes extra compute to insert
arr.insert(1, 7)
print(arr)

#fast to just replace existing
arr[0] = 0
arr[3] =99
print(arr)

print(arr[-1]) # This will read the last value
print(arr[-2]) # This will read the second to last value



# Sublists- slicing array:
print (arr[1:3])

#unpacking:

a,b, c=[1,3,4]



# To make an n length array:
n=9
arr = [1]*n
print (arr)

# reverse:

revarr=[1,8,100]
revarr.reverse()
print(revarr)


#sorting:

arr=[8,1, 3, 2, 9, 100, 230, 110]

arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

# # Sort strings:
arrstr=["bob", "alice", "mary"]
arrstr.sort()
print(arrstr)


# List comprehension
arr=[i+i for i in range(5)]
print(arr)



#2_D List - this will build a 4x4 grid of all 0
arr=[[0]*4 for i in range(4)]
print(arr)

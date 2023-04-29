# While loops

n = 0

while n < 7:
    print("n is less than 7: n="+str(n))
    n+=1
    

# For loops

for i in range(5):
    print(i)

print("i range 2-8")

for i in range(2,9):
    print(i)


# For loop to decrement rather than increment
print ("Decrement loop")

for i in range(5,1, -1):
    print(i)



# Loop through array:
print("looping arrays")
nums=[1,3,4,7]

#Using an index:
for i in range(len(nums)):
    print(nums[i])

#Without index:

for n in nums:
    print(n)

# W index value:
# First- i is the index, and the n is the value:
for i, n in enumerate(nums):
    print (i,n)



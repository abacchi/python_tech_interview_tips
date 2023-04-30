# How do you find the smallest and largest numbers in an unsorted array? 

array = [1.99, 1.01, 2.5, 1.5, 0.01, 99, 55, 1.3, 44, 29, 11, 22]

stackmin = array[0]
stackmax = array[0]

for x in array:
    if x < stackmin:
        stackmin=x
        print("min")
    if x > stackmax:
        stackmax=x
        print("max")


print("Min is "+str(stackmin))
print("Max is "+str(stackmax))


# hash sets
# Cant have any duplicates

myset=set()
myset.add(3)
myset.add(99)
print(myset)

print(len(myset))

# Can search if something is in the set:
print(1 in myset)
print(99 in myset)

myset.remove(99)
print(99 in myset)


# List to a set:
print(set([1, 2, 4]))
# Set comprehension:
myset={i for i in range(8)}
print(myset)


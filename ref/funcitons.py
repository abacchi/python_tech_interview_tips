# Funcitons

def functt(n,m):
    return n*m

print(functt(3,9))




# Nested functions:

def outer(a,b):
    c="cd"

    def innner():
        return a+b+c
    return innner()

print(outer("a","b"))

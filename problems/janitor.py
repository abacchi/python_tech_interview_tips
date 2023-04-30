# From https://www.hackerrank.com/blog/coding-interview-questions-programmers-should-know/

    # The janitor of a high school is extremely efficient. By the end of each day, all of the school’s 
    # waste is in plastic bags weighing between 1.01 pounds and 3.00 pounds. 
    # All plastic bags are then taken to the trash bins outside. 
    # One trip is described as selecting a number of bags which together do not weigh more than 3.00 pounds, 
    # dumping them in the outside trash can and returning to the school. Given the number of plastic bags, and the weights of each bag, 
    # determine the minimum number of trips the janitor has to make.\\

# Given weights : [1.99, 1.01, 2.5, 1.5, 1.01]

from collections import deque

bags = [1.99, 1.01, 2.5, 1.5, 1.01]
bags.sort()

maxweight = 3

trips=0
bagq=deque(bags)


# # Practicing popping
# leftp=bagq.popleft()

print(bagq)
while len(bagq) >= 1:

    if bagq[0]+bagq[len(bagq)-1] > 3:
        bagq.pop()
    else:
        bagq.pop()
        bagq.popleft()
    print(bagq)
    trips+=1
    print(trips)


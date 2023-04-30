# queues (Double ended queues)

from collections import deque

queue= deque()

queue.append(1)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(8)
print(queue)

queue.pop()
print(queue)


listedq=deque([1,2,5])

print(listedq)

# Practicing popping


leftp=listedq.popleft()

print(leftp)

print(listedq)
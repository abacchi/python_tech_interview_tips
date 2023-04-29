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

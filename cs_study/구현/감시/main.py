from collections import deque
queue = deque([(-1,0), (1,0)])
queue.rotate(-1)
print(queue)
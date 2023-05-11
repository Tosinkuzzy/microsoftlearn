# Adding and removing from list
from collections import deque
queue = deque(["Eric", "John", "Micheal"])
queue.append("Terry")
queue.append("Tosinkuzzy")
queue.append("Nextking")
queue.popleft()
queue.popleft()
queue.popleft()
queue
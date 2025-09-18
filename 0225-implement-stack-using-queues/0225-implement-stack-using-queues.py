from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    # Push element onto stack
    def push(self, x):
        self.q.append(x)
        # Rotate all previous elements behind the new one
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    # Remove top element
    def pop(self):
        if self.empty():
            return -1
        return self.q.popleft()

    # Get top element
    def top(self):
        if self.empty():
            return -1
        return self.q[0]

    # Check if stack is empty
    def empty(self):
        return len(self.q) == 0

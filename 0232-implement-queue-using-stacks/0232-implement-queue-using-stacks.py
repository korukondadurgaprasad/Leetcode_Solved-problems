class MyQueue(object):

    def __init__(self):
        # stack_in: for push operations
        # stack_out: for pop/peek operations
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element
        :rtype: int
        """
        if self.empty():
            return -1  # Queue is empty

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """
        Get the front element
        :rtype: int
        """
        if self.empty():
            return -1  # Queue is empty

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out

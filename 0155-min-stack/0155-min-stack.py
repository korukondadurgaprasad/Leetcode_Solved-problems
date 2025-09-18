class MinStack:
    def __init__(self):
        self.st = []                     # internal stack holds (value, min_so_far)

    def push(self, value):
        if not self.st:                  # first element
            self.st.append((value, value))
            return
        mini = min(self.getMin(), value) # get min up to now
        self.st.append((value, mini))

    def pop(self):
        self.st.pop()                    # pop the top tuple

    def top(self):
        return self.st[-1][0]            # first item of top tuple

    def getMin(self):
        return self.st[-1][1]            # second item of top tuple (current min)

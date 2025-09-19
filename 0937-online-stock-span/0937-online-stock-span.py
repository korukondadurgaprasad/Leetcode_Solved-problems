class StockSpanner:
    def __init__(self):
        # Stack to store pairs (price, span)
        self.stack = []

    def next(self, price):
        # Current span
        span = 1

        # Pop elements from stack while current price >= top of stack
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped element
            span += self.stack.pop()[1]

        # Push current price with its span
        self.stack.append((price, span))

        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
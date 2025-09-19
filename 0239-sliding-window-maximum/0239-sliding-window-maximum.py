from collections import deque

class Solution:
    # Function to get the maximum sliding window
    def maxSlidingWindow(self, arr, k):
        
        n = len(arr) # Size of array
        
        # To store the answer
        ans = []
        
        # Deque data structure
        dq = deque()
        
        # Traverse the array
        for i in range(n):
            
            # Update deque to maintain current window
            if dq and dq[0] <= (i - k):
                dq.popleft()
            
            # Maintain the monotonic (decreasing) 
            # order of elements in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # Add current element's index to the deque
            dq.append(i)
            
            # Store the maximum element from 
            # the first window possible
            if i >= (k - 1):
                ans.append(arr[dq[0]])
        
        # Return the stored result
        return ans

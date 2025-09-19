class Solution:
    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        n = len(heights)  # Size of array
        
        # Stack 
        st = []
        
        # To store largest area
        largestArea = 0
        
        # To store current area
        area = 0
        
        # To store the indices of next 
        # and previous smaller elements
        nse = pse = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements is not the smaller element
            while st and heights[st[-1]] >= heights[i]:
                
                # Get the index of top of stack
                ind = st.pop()
                
                # Update the index of previous smaller element
                pse = st[-1] if st else -1
                
                # Next smaller element index for \
                # the popped element is current index
                nse = i
                
                # Calculate the area of the popped element
                area = heights[ind] * (nse - pse - 1)
                
                # Update the maximum area
                largestArea = max(largestArea, area)
            
            # Push the current index in stack
            st.append(i)
        
        # For elements that are not popped from stack
        while st:
            
            # NSE for such elements is size of array
            nse = n
            
            # Get the index of top of stack
            ind = st.pop()
            
            # Update the previous smaller element
            pse = st[-1] if st else -1
            
            # Calculate the area of the popped element
            area = heights[ind] * (nse - pse - 1)
            
            # Update the maximum area
            largestArea = max(largestArea, area)
        
        # Return largest area found
        return largestArea


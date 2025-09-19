class Solution:
    # Function to find the indices of next smaller elements
    def findNSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            currEle = arr[i]
            while st and arr[st[-1]] >= currEle:
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans

    # Function to find the indices of next greater elements
    def findNGE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            currEle = arr[i]
            while st and arr[st[-1]] <= currEle:
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans

    # Function to find the indices of previous smaller or equal elements
    def findPSEE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        for i in range(n):
            currEle = arr[i]
            while st and arr[st[-1]] > currEle:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    # Function to find the indices of previous greater or equal elements
    def findPGEE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        for i in range(n):
            currEle = arr[i]
            while st and arr[st[-1]] < currEle:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    # Function to find the sum of the minimum value in each subarray
    def sumSubarrayMins(self, arr):
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        n = len(arr)
        total_sum = 0
        for i in range(n):
            left = i - psee[i]     # how many to the left
            right = nse[i] - i     # how many to the right
            freq = left * right
            total_sum += freq * arr[i]
        return total_sum

    # Function to find the sum of the maximum value in each subarray
    def sumSubarrayMaxs(self, arr):
        nge = self.findNGE(arr)
        pgee = self.findPGEE(arr)
        n = len(arr)
        total_sum = 0
        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            freq = left * right
            total_sum += freq * arr[i]
        return total_sum

    # Function to find the sum of subarray ranges in each subarray
    def subArrayRanges(self, arr):
        return self.sumSubarrayMaxs(arr) - self.sumSubarrayMins(arr)


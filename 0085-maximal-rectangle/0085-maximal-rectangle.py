class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        st = []
        largestArea = 0

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                ind = st.pop()
                pse = st[-1] if st else -1
                nse = i
                area = heights[ind] * (nse - pse - 1)
                largestArea = max(largestArea, area)
            st.append(i)

        # handle remaining bars
        while st:
            ind = st.pop()
            pse = st[-1] if st else -1
            nse = n
            area = heights[ind] * (nse - pse - 1)
            largestArea = max(largestArea, area)

        return largestArea

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        # convert to int heights
        heights = [0] * m
        maxArea = 0

        for i in range(n):
            for j in range(m):
                # add to height if '1', else reset
                if matrix[i][j] == '1' or matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            # compute max rectangle for this row’s histogram
            area = self.largestRectangleArea(heights)
            maxArea = max(maxArea, area)

        return maxArea

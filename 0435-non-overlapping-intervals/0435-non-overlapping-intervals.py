class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # Step 1: Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize
        n = len(intervals)
        cnt = 1  # count of non-overlapping intervals selected
        last_end = intervals[0][1]  # end time of first interval

        # Step 3: Iterate through the intervals
        for i in range(1, n):
            if intervals[i][0] >= last_end:
                cnt += 1
                last_end = intervals[i][1]

        # Step 4: Minimum intervals to remove = total - selected
        return n - cnt

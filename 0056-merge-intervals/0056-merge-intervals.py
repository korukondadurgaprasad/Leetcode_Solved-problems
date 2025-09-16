class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])   # 1️⃣
        res = []
        current = intervals[0]              # 2️⃣

        for i in range(1, len(intervals)):   # 3️⃣
            if intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
            else:
                res.append(current)
                current = intervals[i]

        res.append(current)                  # 4️⃣
        return res

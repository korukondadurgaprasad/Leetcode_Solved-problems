class Solution(object):
    def findLucky(self, arr):
        lucky_num=-1
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                lucky_num=max(lucky_num,arr[i])
        return lucky_num
        
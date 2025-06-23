class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count=0
        window=sum(arr[:k])
        if window/k >=threshold:
            count+=1
        for i in range(k,len(arr)):
            window = window-arr[i-k]+arr[i]
            if window/k >=threshold:
                count+=1
        return count
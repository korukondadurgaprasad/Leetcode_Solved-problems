class Solution(object):
    def maxProfit(self, prices):
        maxpro=0
        mini=float('inf')
        for i in range(len(prices)):
            mini=min(prices[i],mini)
            maxpro=max(maxpro,prices[i]-mini)
        return maxpro
        
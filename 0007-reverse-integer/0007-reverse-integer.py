class Solution(object):
    def reverse(self, x):
      min = (-2**31)
      max=(2**31)-1
      if x<0:
        sign=-1
      else:
        sign =1
      x=abs(x)
      res =int(str(x)[::-1])*sign
      
      if res<min or res>max:
        return 0
      else:
        return res
# In this case, both the time complexity (TC) and space complexity (SC) are O(log n)

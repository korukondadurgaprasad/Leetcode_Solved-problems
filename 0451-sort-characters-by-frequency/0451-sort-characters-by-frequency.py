class Solution(object):
    def frequencySort(self, s):
        dict={}
        res=""
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        s= sorted(dict, key=dict.get,reverse=True)
        for char in s:
            res=res+char*dict[char]
        return res
        
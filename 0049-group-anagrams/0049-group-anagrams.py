from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        mapi = defaultdict(list)  # ✅ fixed here
        for word in strs:
            a = "".join(sorted(word))  # sorted string used as key
            mapi[a].append(word)
        return list(mapi.values())

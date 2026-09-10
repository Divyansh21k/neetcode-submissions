class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = {}
        len2 = {}
        for i in s:
            if i in len1:
                len1[i]+=1
            else:
                len1[i] =1
        for j in t:
            if j in len2:
                len2[j]+=1
            else:
                len2[j] = 1
        if len1 == len2:
            return True
        return False
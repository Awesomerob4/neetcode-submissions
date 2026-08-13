class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        maxLength = 0
        for r in range(0,len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l=l+1
            mySet.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength
        
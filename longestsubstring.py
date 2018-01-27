class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        Lstr = 0
        usedchar = {}
        for i,c in enumerate(s):
            if c in usedchar and start <= usedchar[c]:
                start = usedchar[c] + 1
            else:
                Lstr = max(Lstr, i - start + 1)
            usedchar[c] = i
                
        return Lstr
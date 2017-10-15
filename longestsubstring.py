class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestnum = 0
        longstr = ""
        tempnum = 0
        tempstr = ""
        keepgo = False
        for x in s:
            if longestnum == 0:
                longstr = x
                longestnum = 1
                continue
            if longestnum > 0:
                if longstr[-1] == x:
                    keepgo = True
                    continue
                if keepgo == True:
                    longstr += x
                    longestnum += 1
                    keepgo = False
            
        return longestnu
            
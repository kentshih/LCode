class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lnum = 0
        lstr = ""
        tnum = 0
        tstr = ""
        keepgo = False
        for i,x in enumerate(s,1):
            print x, tnum

            tnum += 1
            tstr += x
            
            if x in lstr:
                continue
            if lnum < tnum:
                lnum = tnum
                lstr = tnum

            
            

        return lnum
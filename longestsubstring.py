class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Lstr = ""
        Tstr = ""
        pos = 0
        for i,c in enumerate(s,1):
            Tstr = c
            pos = i-1
            for j in xrange(i,len(s)):
                if s[j] not in Tstr:
                    if j == pos+1:
                        Tstr += s[j]
                        pos += 1
                else:
                    break
            print c, i, Tstr
            
            if len(Tstr) > len(Lstr):
                Lstr = Tstr
        
        return len(Lstr)
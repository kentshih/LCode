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
            Tstr = s[i]
            pos = i-1
            # i = 1
        # while i < len(s):
            for j in xrange(i,len(s)):
                if s[j] not in Tstr:
                    if j == pos+1:
                        Tstr += s[j]
                        pos += 1
                else:
                    if len(Tstr) > len(Lstr):
                        Lstr = Tstr
                    # i = pos
                    Tstr = s[i]
                    break


        return len(Lstr)
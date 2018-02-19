class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        maxlen = 0
        n = len(s)
        if n == 0:
            return 0
        for i in xrange(n):
            if i - maxlen >= 1 and s[ i-maxlen-1 : i+1 ] == s[i-maxlen-1 : i+1][::-1]:
                start = i-maxlen-1
                maxlen += 2
                continue
            if i - maxlen >= 0 and s[ i-maxlen : i+1 ] == s[i-maxlen : i+1][::-1]:
                start = i-maxlen
                maxlen += 1

        return s[start:start+maxlen]
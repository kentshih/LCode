class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        count = 0
        while count < len(s):
            if s[count] == p[count]:
                count += 1
            if p[count] == "." 
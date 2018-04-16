class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        lt = {}
        
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        while i
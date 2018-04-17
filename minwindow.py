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
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):    
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1
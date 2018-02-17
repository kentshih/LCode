class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        stack = ""
        maxlen = 0
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] == s[j]:
                start = i
                end = j
                while i != j:
                    if s[i] == s[j]:
                        i += 1
                        j -= 1
                        continue
                    else:
                        break
                if s[i] == s[j]:
                    if len(ans) < end - start:
                        ans = s[start:end]
            i += 1
        return maxlen

    def helper(self, s, l, r):
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        stack = ""
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
        return ans
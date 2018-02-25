class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = [[],[],"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        if digits == "":
            return []
        ans = ['']
        for c in digits:
            tmp = []
            for y in ans:
                for x in kvmaps[c]:
                    tmp.append(y+x)
            ans = tmp
        return ans
    """
        for i in xrange(len(digits)):
            num = int(digits[i])
            for j in xrange(len(letters[num])):
                ans.append("")
            for j in xrange(len(letters[num])):
                ans[j] += letters[num][j]
        return ans
    """
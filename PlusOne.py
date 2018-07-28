class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = True
        ans = []
        for num, i in enumerate(digits[::-1]):
            if plus == True:
                if i == 9:
                    ans = [0] + ans
                    if num == len(digits) - 1:
                        ans = [1] + ans
                        plus = False
                else:
                    ans = [i+1] + ans
                    plus = False
                continue
            else:
                ans = [i] + ans
            print ans
                
        return ans
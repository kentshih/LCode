class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = 999
        ans = 0
        p1 = p2 = p3 = 0
        n = len(nums)
        for i in xrange(0,len(nums)-2):
            l = i+1
            r = n-1
            
            while l != r:
                p1 = nums[i]
                p2 = nums[l]
                p3 = nums[r]
                s = p1 + p2 + p3
                # print p1,p2,p3,s
                if abs(target - s) < diff:
                    ans = s
                    diff = abs(target - s)
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return ans
                
        return ans
            
            
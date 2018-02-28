class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        p1 = p2 = p3 = p4 = 0
        print nums
        for i in xrange(n-3):
            if i != 0 and nums[i] == nums[i-1] :
                continue
            p1 = nums[i]
            for j in xrange(i+1, n-2):
                if nums[j] == nums[j-1] and j != i+1:
                    continue
                p2 = nums[j]
                l = j+1
                r = n-1
                while l != r:
                    p3 = nums[l]
                    p4 = nums[r]
                    s = p1 + p2 + p3 + p4
                    
                    
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    elif s == target:
                        ans.append([p1,p2,p3,p4])
                        print i, j, l, r
                        print p1,p2,p3,p4
                        while nums[r] == nums[r-1] and r > l:
                            r -= 1
                        while nums[l] == nums[l+1] and l < r:
                            l += 1
                        if l < r:
                            l += 1
                        
                        
                            
        return ans
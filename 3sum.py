class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        p1 = 0
        p2 = 1
        p3 = len(nums) - 1
        ans = []
        nums.sort()
        while p1 < len(nums)-2:
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                p1 += 1
                continue
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                s = nums[p1] + nums[p2] + nums[p3]

                if s < 0:
                    p2 += 1
                elif s > 0:
                    p3 -= 1
                else:
                    ans.append([nums[p1],nums[p2],nums[p3]])
                    while p2 < p3 and nums[p2] == nums[p2+1]:
                        p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3-1]:
                        p3 -= 1
                    p2 += 1
                    p3 -= 1
            p1 += 1
        return ans
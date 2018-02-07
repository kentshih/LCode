class Solution(object):
    def getm(target,num):
        if target * 10 % 10 == 0:
            return num[target-1]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        nums = []
        
        target = (n+m) / 2.0
        count = 0
        while count <= target:
            if not nums1 and nums2:
                nums.append(nums2[0])
                nums2 = nums2[1:]
            elif not nums2 and nums1:
                nums.append(nums1[0])
                nums1 = nums1[1:]
            elif nums1[0] <= nums2[0]:
                nums.append(nums1[0])
                nums1 = nums1[1:]
            else:
                nums.append(nums2[0])
                nums2 = nums2[1:]
            count += 1
        #     print nums
        # print target
        # print count
        if target * 10 % 10 > 0:
            return nums[count-1]
        else:
            return (nums[count-2] + nums[count-1]) / 2.0
            
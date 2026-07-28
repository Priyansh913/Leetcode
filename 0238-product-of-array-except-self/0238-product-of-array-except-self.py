class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = []

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])

        right = [1 for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        ans = []

        for i in range(len(nums)):
            ans.append(left[i] * right[i])

        return ans

sol = Solution()
nums = [1,2,3,4]

sol.productExceptSelf(nums)
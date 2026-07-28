class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_sum, max_sum = 0, nums[0]

        for i in range(len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])

            if cur_sum > max_sum:
                max_sum = cur_sum
            
        return max_sum

sol = Solution()
nums = [8, -19, 5, -4, 20]

sol.maxSubArray(nums)
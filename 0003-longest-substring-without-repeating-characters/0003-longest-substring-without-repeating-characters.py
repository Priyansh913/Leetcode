class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charset = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

s = "mq"
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
        
s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
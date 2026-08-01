class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower().replace(" ", "")
        
        for ch in s:
            if not ch.isalnum():
                s = s.replace(ch, "")

        return s == s[::-1]
        
s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
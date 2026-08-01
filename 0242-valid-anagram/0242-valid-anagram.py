from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if Counter(s) == Counter(t):
            return True
        
        else:
            return False


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
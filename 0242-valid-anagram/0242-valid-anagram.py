from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_list = dict(Counter(s))
        t_list = dict(Counter(t))

        s_list = dict(sorted(s_list.items()))
        t_list = dict(sorted(t_list.items()))

        if s_list == t_list:
            return True
        
        else:
            return False


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
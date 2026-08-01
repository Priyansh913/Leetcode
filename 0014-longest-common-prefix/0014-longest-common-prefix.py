class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]
        
        i = 1
        while i < len(strs):
            current = strs[i]

            if current.startswith(prefix):
                i += 1

            else:
                prefix = prefix[:-1]

        return prefix

        

strs = ["flower","flow","flight"]
sol = Solution()
sol.longestCommonPrefix(strs)
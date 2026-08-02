from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashmap = {}
        
        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))

            if temp not in list(hashmap.keys()):
                hashmap[temp] = [strs[i]]

            else:
                hashmap[temp].append(strs[i])

        return list(hashmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
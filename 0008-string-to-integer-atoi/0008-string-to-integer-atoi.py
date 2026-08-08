class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        MIN = -2147483648
        MAX =  2147483647

        is_neg = None
        nums = 0
                

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        while i < len(s):
            if s[i] == "-":
                is_neg = True
                i += 1
                break

            elif s[i] == "+":
                is_neg = False
                i += 1
                break

            else:
                break

        while i < len(s):
            if s[i].isdigit():
                nums = nums * 10 + int(s[i])

            else:
                break

            i += 1

        if is_neg:
            nums = nums * -1

        if nums < MIN: nums = MIN
        if nums > MAX: nums = MAX

        return nums     

s = " -042"
sol = Solution()
print(sol.myAtoi(s))
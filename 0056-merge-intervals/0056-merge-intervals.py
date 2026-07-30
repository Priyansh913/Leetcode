class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sorting the Interval's List
        intervals.sort(key=lambda x: x[0])

        idx = 0
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if idx < len(intervals) and intervals[i][0] <= result[idx][1]:
                start = min(intervals[i][0], result[idx][0])
                end = max(intervals[i][1], result[idx][1])

                result[idx] = [start, end]

            else:
                result.append([intervals[i][0], intervals[i][1]])
                idx += 1

        return result

intervals = [[1, 6], [8, 10], [15, 18]]
sol = Solution()
print(sol.merge(intervals))
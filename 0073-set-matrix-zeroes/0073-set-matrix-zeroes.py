class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        first_row_zero, first_col_zero = 0, 0

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_zero = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        if first_row_zero:
            matrix[0] = [0 for _ in range(len(matrix[0]))]

        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                         
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
sol.setZeroes(matrix)
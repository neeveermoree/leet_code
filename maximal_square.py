class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        lowest_dimension = min(rows, cols)
        for dimensions in range(lowest_dimension, 0, -1):
            for i in range(rows-dimensions+1):
                for j in range(cols-dimensions+1):
                    submatrix = [_[j:(j+dimensions)] for _ in matrix[i:(i+dimensions)]]
                    check = self.check_elements(submatrix)
                    if check is True:
                        return str(dimensions**2)
        return "0"

    def check_elements(self, submatrix):
        n = len(submatrix)
        for i in range(n):
            for j in range(n):
                if submatrix[i][j] != '1':
                    return False
        return True


matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

sol = Solution()
print(sol.maximalSquare(matrix))

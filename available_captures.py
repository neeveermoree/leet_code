# 999. Available Captures for Rook
class Solution:
    def numRookCaptures(self, board) -> int:
        x, y = self.find_rook(board)
        c = 0
        left_idx = x - 1
        while left_idx > -1:
            if board[left_idx][y] == 'B':
                left_idx = 0
            elif board[left_idx][y] == 'p':
                left_idx = 0
                c += 1
            left_idx -= 1

        right_idx = x + 1
        while right_idx < 8:
            if board[right_idx][y] == 'B':
                right_idx = 7
            elif board[right_idx][y] == 'p':
                right_idx = 7
                c += 1
            right_idx += 1

        up_idx = y - 1
        while up_idx > -1:
            if board[x][up_idx] == 'B':
                up_idx = 0
            elif board[x][up_idx] == 'p':
                up_idx = 0
                c += 1
            up_idx -= 1

        down_idx = y + 1
        while down_idx < 8:
            if board[x][down_idx] == 'B':
                down_idx = 7
            elif board[x][down_idx] == 'p':
                down_idx = 7
                c += 1
            down_idx += 1

        return c

    def find_rook(self, board):
        N = 8
        # Find rook
        rook_x = 0
        while rook_x < N:
            rook_y = 0
            while rook_y < N:
                if board[rook_x][rook_y] == 'R':
                    return rook_x, rook_y
                rook_y += 1
            rook_x += 1
        return -1, -1

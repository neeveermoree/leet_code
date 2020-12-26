class Solution:
    def mostVisited(self, n, rounds):
        times_visited = [0] * n
        rounds_amount = len(rounds)
        sector_idx = 0
        while sector_idx < rounds_amount-1:
            for i in range(rounds[sector_idx], rounds[sector_idx+1]+1):
                i = i % (n+1)
                times_visited[i] += 1
            sector_idx += 1

        max_idx = []
        max_val = -1
        for i in range(n):
            if times_visited[i] > max_val:
                max_idx = []
                max_val = times_visited[i]
            elif times_visited[i] == max_val:
                max_idx.append(i)
        return max_idx


sol = Solution()
print(sol.mostVisited(4, [1, 3, 1, 2]))

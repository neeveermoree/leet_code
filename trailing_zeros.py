class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        for i in range(1, n+1):
            if i % 5 == 0:
                fives += self.five_amount(i)
        return fives

    def five_amount(self, n):
        if n % 5 != 0:
            return 0
        return 1 + self.five_amount(n // 5)

    def fact(self, n):
        if n == 0:
            return 1
        return n * self.fact(n-1)


n = int(input())
sol = Solution()
print(sol.trailingZeroes(n))

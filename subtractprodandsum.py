class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        su = 0
        prod = 1
        for char in s:
            num = int(char)
            su += num
            prod *= num
        return prod - su
    
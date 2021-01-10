class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        d = 0
        for i in range(length-2):
            for k in range(i+2, length):
                for j in range(i+1, k):
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        d += 1
        return d

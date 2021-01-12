class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            self.flip(A[i])
        return A
    
    def flip(self, arr):
        length = len(arr)
        i = 0
        while i < (length // 2):
            arr[i], arr[length-i-1] = arr[length-i-1], arr[i]
            i += 1
        for i in range(length):
            arr[i] = 0 if arr[i] == 1 else 1

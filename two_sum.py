# Brute force solution (O(n**2) complexity)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == new_target:
                    first_number = i
                    second_number = j
                    break
        return [first_number, second_number]


# Using hash-table for O(1) look-up time 
# Now complexity is O(n) as well as used memory
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                j = hash_table[complement]
                if i != j:
                    return [i, j]


# One pass solution also with hash-table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, number in enumerate(nums):
            complement = target - number
            if complement in hash_table:
                j = hash_table[complement]
                if idx != j:
                    return [idx, j]
            hash_table[number] = idx

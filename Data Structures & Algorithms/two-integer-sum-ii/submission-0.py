class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        n = len(numbers) - 1
        
        while l <  len(numbers) and n > 0:
            if numbers[l] + numbers[n] < target:
                l += 1
            elif numbers[l] + numbers[n] > target:
                n -= 1
            elif numbers[l] + numbers[n] == target:
                return [(l + 1), (n + 1)]
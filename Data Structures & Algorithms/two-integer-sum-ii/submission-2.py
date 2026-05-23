class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        n = len(numbers) - 1
        
        while l < n:
            current_sum = numbers[l] + numbers[n]

            if current_sum < target:
                l += 1
            elif current_sum > target:
                n -= 1
            elif current_sum == target:
                return [(l + 1), (n + 1)]
    

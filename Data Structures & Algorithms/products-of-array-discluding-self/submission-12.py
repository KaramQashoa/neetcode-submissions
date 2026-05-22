class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin_nums = [0] * len(nums)
        total_prod = 1
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                total_prod *= nums[i]

        if len(nums) == zero_count:
            return fin_nums
        
        if zero_count == 1:
            for i in range (len(fin_nums)):
                if nums[i] == 0:
                    fin_nums[i] = total_prod
                else:
                    fin_nums[i] = 0

        elif  zero_count > 1:
            return fin_nums
            
        else:
            for i in range (len(fin_nums)):
                fin_nums[i] = (int) (total_prod / nums[i])
    
        return fin_nums
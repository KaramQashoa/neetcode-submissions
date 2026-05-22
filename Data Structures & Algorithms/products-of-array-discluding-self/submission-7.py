class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin_nums = [0 for i in range(len(nums))]

        sum = 1
        dec = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                dec[i] = 0
            else:
                sum *= nums[i]

        if len(nums) == len(dec):
            sum = 0
        

        if len(dec) == 1:
            for i in range (len(fin_nums)):
                if i in dec:
                    fin_nums[i] = sum
                else:
                    fin_nums[i] = 0

        elif  len(dec) > 1:
            for i in range (len(fin_nums)):
                fin_nums[i] = 0
            
        else:
            for i in range (len(fin_nums)):
                fin_nums[i] = (int) (sum / nums[i])
    
        return fin_nums
             

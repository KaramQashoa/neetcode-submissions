class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        fin_num_cons = 0

        for num in set_nums:
            next_num = num
            num_cons = 1
            if num - 1 in set_nums:
                continue
            else:
                while next_num + 1 in set_nums:
                    num_cons += 1
                    next_num += 1
            
            if num_cons >= fin_num_cons:
                fin_num_cons = num_cons
        

        return fin_num_cons

        
        
        

        
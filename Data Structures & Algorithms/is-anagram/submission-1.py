class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_1 = {}

        for s_1 in s:
            if s_1 in str_1:
                str_1[s_1] += 1
            else:
                str_1[s_1] = 1
        
        for s_2 in t:
            if s_2 in str_1:
                str_1[s_2] -= 1
            else:
                return False
        
        for i in str_1:
            if str_1[i] != 0:
                return False

            
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst_s = []

        for ch in s:
            if ch >= 'A' and ch <= 'Z':
                lst_s.append(ch.upper())
            if ch >= 'a' and ch <= 'z':
                lst_s.append(ch.upper())
            if ch >= '0' and ch <= '9':
                lst_s.append(ch.upper())
        

        for i in range(len(lst_s)):
            if lst_s[i] != lst_s[(len(lst_s) - 1) - i]:
                return False

        return True

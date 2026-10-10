class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_char = "" 
        for i in s:
            if i.isalnum():
                only_char = only_char + i.lower()
        if only_char == only_char[::-1]:
            return True
        else:
            return False
        
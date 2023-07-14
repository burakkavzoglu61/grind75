class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""

        for elem in s:
            if not elem.isalnum():
                continue
            clean_string+=elem.lower()

        start, end = 0, len(clean_string)-1
        while start<end:
            if clean_string[start]!=clean_string[end]:
                return False
            start+=1
            end-=1
        return True
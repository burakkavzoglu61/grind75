class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencies = {}

        for elem in magazine:
            if elem not in frequencies:
                frequencies[elem] = 1
            else:
                frequencies[elem] += 1

        for elem in ransomNote:
            if elem not in frequencies:
                return False
            if frequencies[elem] == 0:
                return False
            frequencies[elem] -= 1
        return True
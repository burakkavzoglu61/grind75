from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        result = []

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in differences.keys():
                result.append(differences[diff])
                result.append(i)
                break
            else:
                differences[nums[i]] = i
        return result

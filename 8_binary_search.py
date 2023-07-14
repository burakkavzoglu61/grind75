from typing import List


class Solution:
    def __binary_search(self, nums, target, start, end):
        if end>=start:
            index = int((start + end) / 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                return self.__binary_search(nums, target, start, index-1)
            else:
                return self.__binary_search(nums, target, index+1, end)
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.__binary_search(nums, target, 0, len(nums) - 1)
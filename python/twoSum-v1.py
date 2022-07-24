class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            for second in range(len(nums)):
                if (first == second):
                    break
                if (nums[first] + nums[second] == target):
                    return([first, second])

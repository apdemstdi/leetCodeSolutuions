class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for num in range(len(nums)):
            hashmap[nums[num]] = num
        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in hashmap and hashmap[difference] != num:
                return[num, hashmap[difference]]

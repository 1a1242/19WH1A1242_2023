class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        se = set()
        for i in range(len(nums)):
            if target-nums[i] in se:
                return [i, nums.index(target-nums[i])]
            else:
                se.add(nums[i])

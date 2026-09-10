class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        digits = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in digits:
                return [digits[complement], i]

            digits[nums[i]] = i
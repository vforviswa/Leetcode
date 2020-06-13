class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums_len = len(nums)
        nums.sort()
        output = [[num] for num in nums]
        for i in range(nums_len):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(output[i]) < len(output[j]) + 1:
                        output[i] = output[j] + [nums[i]]
        return max(output, key=len)
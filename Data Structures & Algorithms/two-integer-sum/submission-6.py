class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # create list
        for i in range(len(nums)):  # Go through each in nums
            needed = target - nums[i]   #What num added gets target?
            if needed in seen:  #Do we have that number
                return [seen[needed], i]    #if we do return that
            seen[nums[i]] = i   #if not add new num to list at postion
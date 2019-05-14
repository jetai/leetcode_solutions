# Given a target, need to find if any numbers in the list summed together equal that val
# Idea 2: Iterate through nums, for each i do (target - i), see if (target - i) is found in rest of the list
#       Runtime: O(n^2)
#       Space complexity: O(1)
# Let's start off with implementing idea 2 first and then working on optimization
# Can I optimize the outer loop?
#   - no i dont think so, we have to loop through every number in nums worst case
# Can I optimize the inner loop? Sacrificing some space for increased runtime
#   - build upon your previous idea of using a created sub_list
# New runtime complexity: O(len(nums)) + O(len(nums)) + O(len(nums)) -> O(n)
# New space complexity: O(n) + O(n) -> O(n)
class Solution:
    def createNumsMap(self, nums):
        nums_map = {}
        for index, num in enumerate(nums):
            nums_map[num] = index
        return nums_map

    def createSubtractList(self, nums, target):
        subtract_list = []
        pos = 0
        for val in nums:
            subtract_list.append(target - val)
        return subtract_list

    def twoSum(self, nums, target):
        nums_map = self.createNumsMap(nums)
        subtract_list = self.createSubtractList(nums, target)
        for index, num in enumerate(subtract_list):
            if num in nums_map and index != nums_map[num]:
                return [index, nums_map[num]]
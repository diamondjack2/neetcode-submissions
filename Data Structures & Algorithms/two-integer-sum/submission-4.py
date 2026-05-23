class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        for i in range(len(nums)):
            y = nums[i]
            for j in range(len(nums)):
                if i != j and y + nums[j] == target:
                    x.append(i)
                    x.append(j)
                    return x
        return x
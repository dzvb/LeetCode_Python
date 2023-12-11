class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        di = {}
        for i, el in enumerate(nums):
            di[el] = i

        for i, el in enumerate(nums):
            residual = target - el
            if residual in di and i != di[residual]:
                return [i, di[residual]]
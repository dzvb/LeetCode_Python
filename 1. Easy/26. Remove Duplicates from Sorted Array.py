class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                # previous unique element = new unqiue
                nums[k] = nums[i] 
                k += 1
        return k
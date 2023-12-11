class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max = len(digits) - 1
        for i in range(max, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # for cases like 9, 99, ...
        return [1] + digits

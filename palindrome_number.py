# Input: Nhap mot so nguyen
# Output: In ra True neu so do la so doi xung, nguoc lai in ra False


class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


# Test nhanh
print(Solution().isPalindrome(121))  # True
print(Solution().isPalindrome(-121))  # False
print(Solution().isPalindrome(10))  # False
print(Solution().isPalindrome(12321))  # True
print(Solution().isPalindrome(0))  # True

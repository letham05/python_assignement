# Input: Nhap mot so nguyen
# Output: In ra True neu so do la so doi xung, nguoc lai in ra False


# Version 1: Original (String Conversion)
class SolutionOriginal:
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


# Version 2: Less Efficient (Reversing Entire Number)
class SolutionLessOptimized:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        original = x
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        return original == reversed_number


# Version 3: Optimized (Reversing Half of the Number)
class SolutionOptimized:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


# Test function to compare all versions
def test_solution():
    original = SolutionOriginal()
    less_optimized = SolutionLessOptimized()
    optimized = SolutionOptimized()

    test_cases = [
        12345,
        121,
        -121,
        10,
        12321,
    ]
    for x in test_cases:
        print(f"Input: {x}")
        print(f"Version 1 : {original.isPalindrome(x)}")
        print(f"Version 3 : {less_optimized.isPalindrome(x)}")
        print(f"Version 2 : {optimized.isPalindrome(x)}")

        print()


# Call the test function
test_solution()

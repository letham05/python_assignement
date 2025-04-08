# Input: Nhap mot so nguyen
# Output: In ra True neu so do la so doi xung, nguoc lai in ra False


# Version 1: Original (String Conversion)
# This version converts the number to a string and checks if it is equal to its reverse.
# It is simple but less efficient due to the overhead of string conversion.
class SolutionOriginal:
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


# Version 2: Optimized (Reversing Half of the Number)
# This version avoids string conversion and reverses only half of the number.
# It is more efficient than reversing the entire number because it stops early
# when the reversed half becomes greater than or equal to the remaining half.
class SolutionOptimized:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


# Version 3: Less Efficient (Reversing Entire Number)
# This version reverses the entire number and compares it with the original.
# It is less efficient than Version 2 because it performs unnecessary operations
# by reversing the entire number even when it is not needed.
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


# Test function to compare all versions
# This function tests all three versions with the same test cases and prints the results.
def test_solution():
    original = SolutionOriginal()
    optimized = SolutionOptimized()
    most_optimized = SolutionLessOptimized()

    test_cases = [121, -121, 10, 12321, 0]
    for x in test_cases:
        print(f"Input: {x}")
        print(f"Version 1 (Original): {original.isPalindrome(x)}")
        print(f"Version 2 (Optimized): {optimized.isPalindrome(x)}")
        print(f"Version 3 (Less Efficient): {most_optimized.isPalindrome(x)}")
        print()


# Call the test function
test_solution()

# Input: Nhap danh sach cac so nguyen
# Output: In ra danh sach cac so "lonely" trong danh sach (lonely tuc la khong co so nao ben trai hoac ben phai)


# Version 1: Using Dictionary for Frequency Count o(n)
class SolutionOriginal:
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dictionary to count the frequency of each number
        freq = {}  # Count the frequency of each number

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []
        for num in nums:
            if freq[num] == 1 and (num - 1 not in freq) and (num + 1 not in freq):
                result.append(num)

        return result


# Version 2: (Using Collections.Counter) o(n)
from collections import Counter

class SolutionOptimized:
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)  # Use Counter to count frequencies
        return [
            num
            for num in nums
            if freq[num] == 1 and (num - 1 not in freq) and (num + 1 not in freq)
        ]


# Version 3:(Single Pass with Set) o(n)
class SolutionMostOptimized:
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)  # Use Counter to count frequencies
        nums_set = set(nums)  # Use a set for quick neighbor checks
        return [
            num
            for num in nums_set
            if freq[num] == 1
            and (num - 1 not in nums_set)
            and (num + 1 not in nums_set)
        ]
        
#using sorted o(nlogn)    
class SolutionSorted:
    def findLonely(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            
            if (i > 0 and nums[i] == nums[i - 1]) or (i < len(nums) - 1 and nums[i] == nums[i + 1]):
                continue
            # 
            if (i > 0 and nums[i] - 1 == nums[i - 1]) or (i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]):
                continue
            result.append(nums[i])
        return result


# Test function to compare all versions
# This function tests all three versions with the same test cases and prints the results.
def test_solution():
    original = SolutionOriginal()
    optimized1 = SolutionOptimized()
    optimized2 = SolutionMostOptimized()
    Sorted3 = SolutionSorted()

    test_cases = [[10, 6, 5, 8], [1, 3, 5, 3], [4, 4, 4, 4], [7, 8, 9, 10]]
    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Version 1 : {original.findLonely(nums)}")
        print(f"Version 2 (Optimized1): {optimized1.findLonely(nums)}")
        print(f"Version 3 (Optimized2): {optimized2.findLonely(nums)}")
        print(f"Version 4 (Sorted3): {Sorted3.findLonely(nums)}")
        print()


# Call the test function
test_solution()

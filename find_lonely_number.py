# Input: Nhap danh sach cac so nguyen
# Output: In ra danh sach cac so "lonely" trong danh sach (lonely tuc la khong co so nao ben trai hoac ben phai)


class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}  # Đếm số lần xuất hiện của mỗi số

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


sol = Solution()
print(sol.findLonely([10, 6, 5, 8]))  # Output: [10, 8]
print(sol.findLonely([1, 3, 5, 3]))  # Output: [1, 5]

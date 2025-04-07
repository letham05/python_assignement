# class Solution:
#     def twoSum(self, nums, target):
#         # Duyệt qua tất cả các cặp phần tử trong mảng
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]  # Trả về chỉ số của hai phần tử
#         return []  # Nếu không tìm thấy cặp nào thỏa mãn

# class Solution:
#     def twoSum(self, nums, target):
#         num_map = {}  # Dùng hashmap để lưu trữ các phần tử và chỉ số của chúng
#         for i, num in enumerate(nums):
#             complement = target - num  # Tính toán số bù
#             if complement in num_map:  # Kiểm tra số bù đã tồn tại trong hashmap chưa
#                 return [num_map[complement], i]  # Nếu có, trả về chỉ số của cặp phần tử
#             num_map[num] = i  # Nếu chưa, lưu phần tử và chỉ số vào hashmap
#         return []  # Nếu không tìm thấy cặp nào thỏa mãn


class Solution:
    def twoSum(self, nums, target):
        # Tạo một mảng chứa giá trị và chỉ số ban đầu
        nums_with_index = [(num, i) for i, num in enumerate(nums)]

        # Sắp xếp mảng theo giá trị của phần tử
        nums_with_index.sort()

        left, right = 0, len(nums) - 1  # Khởi tạo con trỏ trái và phải

        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]

            if current_sum == target:  # Nếu tổng bằng target, trả về chỉ số của chúng
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif (
                current_sum < target
            ):  # Nếu tổng nhỏ hơn target, di chuyển con trỏ trái sang phải
                left += 1
            else:  # Nếu tổng lớn hơn target, di chuyển con trỏ phải sang trái
                right -= 1

        return []  # Nếu không tìm thấy cặp nào thỏa mãn


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

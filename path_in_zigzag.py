# Input: Nhập một số nguyên label
# Output: In ra danh sách các node trên đường đi từ label về gốc cây theo cấu trúc zigzag


# # Version 1: Sử dụng precomputed levels
# class SolutionOptimized1:
#     def pathInZigZagTree(self, label):
#         result = []
#         level = 0

#         # Tìm level của node
#         while (1 << level) <= label:
#             # Tính toán số lượng node trong level hiện tại
#             # số lượng node trong level hiện tại là 2^level
#             # in ra số lượng node trong level hiện tại
#             print(f"Level {level}: {1 << level} nodes")
#             level += 1

#         while label >= 1:
#             result.append(label)
#             level -= 1
#             # Tính start và end của level hiện tại
#             start = 1 << level
#             print (f"Start of level {level}: {start}")
#             end = (1 << (level + 1)) - 1
#             print (f"End of level {level}: {end}")
#             # Tìm node cha ở cây zigzag
#             label = start + end - label
#             print (label)
#             label //= 2
            

        # return result[::-1]  # Đảo ngược kết quả để trả về từ gốc đến label


# Version 2: Dùng Bitwise (tối ưu hơn)
class SolutionOptimized2:
    def pathInZigZagTree(self, label):
        result = []
        # bit_length là số bit cần thiết để biểu diễn label
        # bin(14) => '0b1110' => 4 bit
        # bit_length(14) => 4
        level = label.bit_length() - 1  # Tính level bằng bit_length()

        while label >= 1:
            result.append(label)
            # Tính toán node cha ở cây zigzag
            label = ((1 << level) + (1 << (level + 1)) - 1 - label) // 2
            level -= 1

        return result[::-1]  # Đảo ngược kết quả để trả về từ gốc đến label


# Hàm kiểm thử để so sánh 2 phiên bản
def test_solution():
    # optimized1 = SolutionOptimized1()
    optimized2 = SolutionOptimized2()

    test_cases = [14, 26, 1, 7, 100, 255]
    for label in test_cases:
        # path1 = optimized1.pathInZigZagTree(label)
        path2 = optimized2.pathInZigZagTree(label)
        print(f"Label: {label}")
        # print(f"  Version 1 (Precomputed Levels): {path1}")
        print(f"  Version 2 (Bitwise Operations): {path2}")
    
# Gọi hàm kiểm thử
test_solution()

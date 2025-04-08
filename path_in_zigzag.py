# Input: Nhap mot so nguyen label
# Output: In ra danh sach cac node tren duong di tu label ve goc cay


# version 1: Original (Less Optimized)
class SolutionOriginal:
    def pathInZigZagTree(self, label):
        result = []
        level = 0
        # Xác định level của label
        while (1 << level) <= label:
            level += 1

        while label >= 1:
            result.append(label)
            level -= 1
            # Tính toán phạm vi của level hiện tại
            start = 1 << level
            end = (1 << (level + 1)) - 1
            # Tính toán parent trong cây reversed
            label = start + end - label
            label //= 2

        return result[::-1]  # Đảo ngược kết quả để trả về từ gốc đến label


# version 2: Optimized with Precomputed Levels
class SolutionOptimized:
    def pathInZigZagTree(self, label):
        result = []
        level = 0
        # Precompute the levels
        while (1 << level) <= label:
            level += 1

        while label >= 1:
            result.append(label)
            level -= 1
            # Precompute the start and end of the current level
            start = 1 << level
            end = (1 << (level + 1)) - 1
            # Calculate the parent in the reversed tree
            label = start + end - label
            label //= 2

        return result[::-1]


# version 3: Most Optimized (Using Bitwise Operations)
class SolutionMostOptimized:
    def pathInZigZagTree(self, label):
        result = []
        level = label.bit_length() - 1  # Tính level trực tiếp bằng bit_length()

        while label >= 1:
            result.append(label)
            # Tính toán parent trong cây reversed
            label = ((1 << level) + (1 << (level + 1)) - 1 - label) // 2
            level -= 1

        return result[::-1]  # Đảo ngược kết quả để trả về từ gốc đến label


# Hàm test
def test_solution():
    original = SolutionOriginal()
    optimized = SolutionOptimized()
    most_optimized = SolutionMostOptimized()

    test_cases = [14, 26, 1, 7]
    for label in test_cases:
        print(f"Label: {label}")
        print(f"version 1: {original.pathInZigZagTree(label)}")
        print(f"version 2: {optimized.pathInZigZagTree(label)}")
        print(f"version 3 {most_optimized.pathInZigZagTree(label)}")
        print()


# Gọi hàm test
test_solution()

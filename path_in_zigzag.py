# Định nghĩa lại lớp Solution
class Solution(object):
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

        return result[::-1]


# Hàm test
def test_solution():
    solution = Solution()

    # Test case 1
    label = 14
    print(f"Path for label {label}: {solution.pathInZigZagTree(label)}")

    # Test case 2
    label = 26
    print(f"Path for label {label}: {solution.pathInZigZagTree(label)}")

    # Test case 3
    label = 1
    print(f"Path for label {label}: {solution.pathInZigZagTree(label)}")

    # Test case 4
    label = 7
    print(f"Path for label {label}: {solution.pathInZigZagTree(label)}")


# Gọi hàm test
test_solution()

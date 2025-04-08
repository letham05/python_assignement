# Input: Nhap chuoi s chua cac ky tu va cac cap ngoac
# Output: In ra chuoi s da duoc dao nguoc cac ky tu trong cac cap ngoac va xoa cac cap ngoac


# Version 1: Original (Stack-Based Approach)
class SolutionOriginal:
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = ""

        for ch in s:
            if ch == "(":
                stack.append(curr)
                curr = ""
            elif ch == ")":
                curr = curr[::-1]
                prev = stack.pop()
                curr = prev + curr
            else:
                curr += ch

        return curr


# Version 2: Optimized (Using List for String Concatenation)
class SolutionOptimized:
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = []

        for ch in s:
            if ch == "(":
                stack.append(curr)
                curr = []
            elif ch == ")":
                curr.reverse()
                prev = stack.pop()
                curr = prev + curr
            else:
                curr.append(ch)

        return "".join(curr)


# Version 3: Most Optimized (Two-Pass Approach)
class SolutionMostOptimized:
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = {}
        stack = []

        # First pass: Find matching parentheses
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                open_idx = stack.pop()
                pair[open_idx] = i
                pair[i] = open_idx

        # Second pass: Traverse and reverse
        result = []
        i, direction = 0, 1
        while i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction *= -1
            else:
                result.append(s[i])
            i += direction

        return "".join(result)


# Test function to compare all versions
def test_solution():
    original = SolutionOriginal()
    optimized = SolutionOptimized()
    most_optimized = SolutionMostOptimized()

    test_cases = ["(u(love)i)", "(abcd)", "(a(bc)d)", "((ab)c)"]
    for s in test_cases:
        print(f"Input: {s}")
        print(f"Version 1 : {original.reverseParentheses(s)}")
        print(f"Version 2 : {optimized.reverseParentheses(s)}")
        print(
            f"Version 3 (Most): {most_optimized.reverseParentheses(s)}"
        )  # Fixed label
        print()


# Call the test function
test_solution()

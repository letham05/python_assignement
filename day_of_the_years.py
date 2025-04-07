class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split("-"))

        # Số ngày mỗi tháng (tháng 2 là 28, sẽ xử lý năm nhuận sau)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Kiểm tra năm nhuận
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29

        # Tính tổng số ngày trước tháng hiện tại + ngày hiện tại
        return sum(days_in_month[: month - 1]) + day


sol = Solution()
print(sol.dayOfYear("2019-01-09"))  # Output: 9
print(sol.dayOfYear("2019-02-10"))  # Output: 41
print(sol.dayOfYear("2000-12-31"))  # Output: 366 (năm nhuận)

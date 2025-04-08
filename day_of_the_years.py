# Version 1: Trung bình - Xử lý thủ công số ngày từng tháng + năm nhuận
class SolutionV1:
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Kiểm tra năm nhuận và cập nhật tháng 2
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29

        return sum(days_in_month[:month - 1]) + day


# Version 2: Tốt hơn - Dùng datetime để lấy ngày thứ bao nhiêu trong năm
from datetime import datetime

class SolutionV2:
    def dayOfYear(self, date):
        dt = datetime.strptime(date, "%Y-%m-%d")
        return dt.timetuple().tm_yday


# Version 3: Rất tốt - Dùng thư viện calendar để lấy số ngày trong mỗi tháng
import calendar

class SolutionV3:
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))
        total_days = sum(calendar.monthrange(year, m)[1] for m in range(1, month))
        return total_days + day


# Version 4: Tối ưu nhất - Không dùng thư viện, không vòng lặp
class SolutionV4:
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))
        # Danh sách tổng số ngày tính đến đầu tháng (năm thường)
        days_to_month = [0, 31, 59, 90, 120, 151, 181,
                         212, 243, 273, 304, 334]
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        return days_to_month[month - 1] + day + (1 if is_leap and month > 2 else 0)


# Hàm kiểm tra 4 phiên bản với các test case
def test_all_versions():
    test_dates = ["2019-01-09", "2019-02-10", "2000-12-31", "2020-03-01", "2024-02-29"]

    print("So sánh kết quả các phiên bản:\n")
    for date in test_dates:
        print(f"Ngày: {date}")
        print("V1:", SolutionV1().dayOfYear(date))
        print("V2:", SolutionV2().dayOfYear(date))
        print("V3:", SolutionV3().dayOfYear(date))
        print("V4:", SolutionV4().dayOfYear(date))
        print("-" * 30)


# Chạy test
test_all_versions()

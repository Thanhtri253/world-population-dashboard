World Population Dashboard 
Ứng dụng trực quan hóa dữ liệu dân số thế giới được xây dựng bằng Python, Dash và Plotly. Ứng dụng cho phép người dùng theo dõi xu hướng tăng trưởng dân số của từng quốc gia và so sánh các quốc gia đông dân nhất theo từng năm.  

## Giới thiệu
Dự án này sử dụng dữ liệu dân số lịch sử (từ năm 1960 đến 2016) để tạo ra một giao diện web tương tác. Người dùng có thể:


Theo dõi xu hướng: Xem biểu đồ đường về sự thay đổi dân số của một quốc gia cụ thể qua các năm.  


So sánh thứ hạng: Xem biểu đồ cột hiển thị Top 10 quốc gia có dân số lớn nhất trong một năm được chọn.  

## Cấu trúc tệp tin

world_population_dashboard.py: Mã nguồn chính của ứng dụng Dash, xử lý logic xử lý dữ liệu và giao diện người dùng.  


CountryPopulation.csv: Tập dữ liệu chứa thông tin dân số của các quốc gia và khu vực từ năm 1960 đến 2016.  

## Yêu cầu hệ thống
Để chạy ứng dụng này, bạn cần cài đặt Python và các thư viện sau:

Bash
pip install pandas dash plotly
## Hướng dẫn sử dụng
Tải cả hai tệp world_population_dashboard.py và CountryPopulation.csv về cùng một thư mục.

Mở terminal hoặc command prompt tại thư mục đó.

Chạy ứng dụng bằng lệnh:

Bash
python world_population_dashboard.py
Truy cập vào địa chỉ http://127.0.0.1:8050/ trên trình duyệt web của bạn để trải nghiệm dashboard.

## Dữ liệu
Dữ liệu đầu vào bao gồm các cột chính:  

Country Name: Tên quốc gia hoặc vùng lãnh thổ.

Country Code: Mã quốc gia (3 chữ cái).

Year (1960 - 2016): Dân số tổng cộng theo từng năm.

## Tính năng kỹ thuật

Tiền xử lý dữ liệu: Sử dụng pandas để chuyển đổi dữ liệu từ dạng bảng rộng (wide format) sang bảng dọc (long format) giúp dễ dàng truy vấn và vẽ biểu đồ.  


Tính tương tác: Sử dụng các thành phần dcc.Dropdown và dcc.Slider của Dash để cập nhật biểu đồ theo thời gian thực mà không cần tải lại trang.  

Dự án được tạo ra nhằm mục đích học tập và thực hành trực quan hóa dữ liệu với Python.

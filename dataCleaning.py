import pandas as pd
import os
import matplotlib.pyplot as plt

# Xóa màn hình console (chỉ áp dụng trên Windows)
os.system('cls')

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('movies.csv')

# Hiển thị tên các cột
print("Các cột trong DataFrame:")
print(df.columns)

# Loại bỏ các cột không cần thiết cho việc xử lý
df = df.drop(['movieId', 'critic_sentiment', 'audience_sentiment', 'audience_score'], axis=1)

# Thay đổi tên các cột thành tiếng Việt
df.columns = ['Nam san xuat', 'Nguon xem phim', 'Ten phim', 'Diem phe binh', 'Ngay ra rap', 'Ngay phat song', 'Danh gia', 'Ngon ngu', 'Thoi luong phim']

# Lọc dữ liệu cho năm 2023
df1 = df[df['Nam san xuat'] == 2023]
df1.reset_index(drop=True, inplace=True)

# Loại bỏ các dòng có giá trị null
df1 = df1.dropna()
df1['Diem phe binh'] /= 10

df1 = df1.drop(['Ngay phat song'], axis=1)

# Chuyển đổi các cột ngày tháng năm thành định dạng dd/mm/yyyy
df1['Ngay ra rap'] = pd.to_datetime(df1['Ngay ra rap'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0], format='%b %d, %Y', errors='coerce').dt.strftime('%d/%m/%Y')

# Kiểm tra kết quả
print(df1.head())

df1 = df1.rename(columns={'Danh gia':'The loai'})

# Lưu dữ liệu vào tệp CSV mới
df1.to_csv('filmCleaned.csv', index=False)
print("File filmCleaned.csv đã được tạo và lưu dữ liệu từ df1.")

# Create một file.csv mới bằng cách cleaningData đã có sẵn và lưu vào một file.csv mới. 
import pandas as pd

# Đọc dữ liệu từ file "movies.csv"
df = pd.read_csv('movies.csv')

# Thay đổi tên cột thành tiếng Việt
df.columns = [
    'Ma phim', 'Nam san xuat', 'Nguon xem phim', 'Ten phim', 
    'Diem phe binh', 'Cam xuc phe binh', 'Diem khan gia', 
    'Cam xuc cua khan gia', 'Ngay ra rap', 'Ngay phat song', 
    'Danh gia', 'Ngon ngu', 'Thoi luong phim'
]

# Lọc dữ liệu cho năm 2023
df1 = df[df['Nam san xuat'] == 2023].reset_index(drop=True)

# Loại bỏ các dòng có giá trị null
df1 = df1.dropna()

# Chuyển đổi cột 'Ngay ra rap' thành định dạng dd/mm/yyyy
df1['Ngay ra rap'] = pd.to_datetime(df1['Ngay ra rap'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0], format='%b %d, %Y', errors='coerce').dt.strftime('%d/%m/%Y')

# Chuyển đổi cột 'Ngay phat song' với định dạng tương tự
df1['Ngay phat song'] = pd.to_datetime(df1['Ngay phat song'].str.extract(r'(\d{1,2}-\w{3}-\d{2})')[0], format='%d-%b-%y', errors='coerce').dt.strftime('%d/%m/%Y')
# Kiểm tra chuyển đổi ngày tháng năm thành định dạng dd/mm/yyyy
print(df1[['Ngay ra rap', 'Ngay phat song']])

# Lưu dữ liệu vào tệp CSV mới để tiến hành phân tích (CRUD).
df1.to_csv('newFileCreatedData.csv', index=False)
print("File newFileCreatedData.csv đã được tạo và lưu dữ liệu từ df1.")

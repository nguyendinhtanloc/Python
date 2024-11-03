import pandas as pd

# Đọc file csv hiện có
df = pd.read_csv('newFileCreatedData.csv')

# 1. Thêm mới dữ liệu vào file.csv có sẵn.
# Tạo một DataFrame mới với dữ liệu cần thêm
# Dữ liệu 1: Phim "Hot Seat"
new_data = pd.DataFrame({
    'Ma phim': ['fc146ab5-27f4-356c-9afa-04688c52c23e'],
    'Nam san xuat': [2022],
    'Nguon xem phim': ['https://www.rottentomatoes.com/m/hot_seat'],
    'Ten phim': ['Hot Seat'],
    'Diem phe binh': [16],
    'Cam xuc phe binh': ['negative'],
    'Diem khan gia': [15],
    'Cam xuc cua khan gia': ['negative'],
    'Ngay ra rap': ['Jul 1, 2022, Limited'],
    'Ngay phat song': ['1-Jul-22'],
    'Danh gia': ['R (Some Violence|Language Throughout)'],
    'Ngon ngu': ['English'],
    'Thoi luong phim': ['1h 44m'],
})

# Dữ liệu 2: Phim "Shattered"
new_movie_data = pd.DataFrame({
    'Ma phim': ['fcad9585-e322-4e96-bdcb-0d967157f2ab'],
    'Nam san xuat': [2022],
    'Nguon xem phim': ['https://www.rottentomatoes.com/m/shattered_2022'],
    'Ten phim': ['Shattered'],
    'Diem phe binh': [19],
    'Cam xuc phe binh': ['negative'],
    'Diem khan gia': [67],
    'Cam xuc cua khan gia': ['positive'],
    'Ngay ra rap': ['Jan 14, 2022, Limited'],
    'Ngay phat song': ['14-Jan-22'],
    'Danh gia': ['R (Language Throughout|Bloody Images|Nudity|Sexual Content|Violence)'],
    'Ngon ngu': ['English'],
    'Thoi luong phim': ['1h 32m'],
})

# Kết hợp dữ liệu mới
new_data = pd.concat([new_data, new_movie_data], ignore_index=True)

# Chuyển đổi định dạng ngày tháng
new_data['Ngay ra rap'] = pd.to_datetime(new_data['Ngay ra rap'].str.replace(', Limited', ''), format='%b %d, %Y', errors='coerce').dt.strftime('%d/%m/%y')
new_data['Ngay phat song'] = pd.to_datetime(new_data['Ngay phat song'], format='%d-%b-%y', errors='coerce').dt.strftime('%d/%m/%y')

# Kết hợp với DataFrame cũ
df_combined = pd.concat([df, new_data], ignore_index=True)

# Sắp xếp theo điểm khán giả tăng dần
df1 = df_combined.sort_values(by='Diem khan gia', ascending=True)

# Lưu dữ liệu mới vào một file CSV mới
df1.to_csv('updated_movies_data.csv', index=False)
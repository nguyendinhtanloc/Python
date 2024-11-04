import pandas as pd

# READ
# Đọc dữ liệu từ file 'movies.csv'.
df = pd.read_csv('movies.csv')

print("-----------------------------------------------------------------")

# CREATE
# Thêm mới dữ liệu vào file movies.csv có sẵn.
# Dữ liệu 1: Tên phim 'Dragon Ball Z'
new_data1 = pd.DataFrame({
    'movieId': ['fc132ab45-27f3-452c-10afc-81841c52c23e'],
    'movieYear': [2024],
    'movieURL': ['https://www.rottentomatoes.com/m/dragon_ball_z'],
    'movieTitle': ['Dragon Ball Z'],
    'critic_score': [5],
    'critic_sentiment': ['positive'],
    'audience_score': [100],
    'audience_sentiment': ['positive'],
    'release_date_theaters': ['Jul 10, 2024, Limited'],
    'release_date_streaming': ['10-Jul-24'],
    'rating': ['R (Very exciting|Interesting)'],
    'original_language': ['English'],
    'runtime': ['1h 56m'],
})

new_data2 = pd.DataFrame({
    'movieId': ['fc343ab45-12f3-654c-10adr-74737c141c23f'],
    'movieYear': [2024],
    'movieURL': ['https://www.rottentomatoes.com/m/dragon_ball_super'],
    'movieTitle': ['Dragon Ball Super'],
    'critic_score': [3],
    'critic_sentiment': ['positive'],
    'audience_score': [78],
    'audience_sentiment': ['positive'],
    'release_date_theaters': ['Oct 8, 2024, Limited'],
    'release_date_streaming': ['8-Oct-24'],
    'rating': ['R (Language Throughout|Bloody Images|Violence)'],
    'original_language': ['English'],
    'runtime': ['1h 19m'],
})

new_data3 = pd.DataFrame({
    'movieId': ['fc414ab2314-24f3-321c-10adv-42424c52c23e'],
    'movieYear': [2024],
    'movieURL': ['https://www.rottentomatoes.com/m/dragon_ball_af'],
    'movieTitle': ['Dragon Ball AF'],
    'critic_score': [2],
    'critic_sentiment': ['positive'],
    'audience_score': [87],
    'audience_sentiment': ['positive'],
    'release_date_theaters': ['May 26, 2024, Limited'],
    'release_date_streaming': ['26-May-24'],
    'rating': ['R (Very exciting|Interesting)'],
    'original_language': ['English'],
    'runtime': ['1h 24m'],
})

# Kết hợp dữ liệu mới.
df = pd.concat([df, new_data1, new_data2, new_data3], ignore_index=True)

# Cập nhật lại vào file.csv (movies.csv)
df.to_csv('NewMovies.csv', index=False)
print("file movies.csv mới đã được tạo trên thao tác create data mới vào movies.csv đã có sẵn.")

print("-----------------------------------------------------------------")

# UPDATE.
# Đổi header sang tiếng việt.
df.columns = [
    'Ma phim', 'Nam san xuat', 'Nguon xem phim', 'Ten phim', 
    'Diem phe binh', 'Cam xuc phe binh', 'Diem khan gia', 
    'Cam xuc cua khan gia', 'Ngay ra rap', 'Ngay phat song', 
    'Danh gia', 'Ngon ngu', 'Thoi luong phim'
]

# Đổi một số dữ liệu tên phim ở dòng 28 (cụ thể từ cột movieTitle (Tên phim), movieURL)).
df.loc[df['Ten phim'] == 'Bobcat Moretti', 'Ten phim'] = 'Chasing Shadows'
df.loc[df['Nguon xem phim'] == 'https://www.rottentomatoes.com/m/bobcat_moretti', 'Nguon xem phim'] = 'https://www.rottentomatoes.com/m/chasing Shadows'
df.loc[df['Diem phe binh'] == 71, 'Diem phe binh'] = 85
df.loc[df['Diem khan gia'] == 94, 'Diem khan gia'] = 64
df.loc[df['Ngay ra rap'] == 'Aug 4, 2023, Limited', 'Ngay ra rap'] = 'May 6, 2023, Wide'
df.loc[df['Ngay phat song'] == '4-Aug-23', 'Ngay phat song'] = '29-Sep-23'

# Ví dụ điền giá trị bị thiếu vào hàng/cột có giá trị (null).
# Tìm vị trí (null) của dòng có tên phim 'Art of love', 'Samaritan' bị thiếu.
art_of_love_row = df[df['Ten phim'] == 'Art of Love'].index[0]
Samaritan = df[df['Ten phim'] == 'Samaritan'].index[0]

# Điền giá trị null bị thiếu.
df.loc[art_of_love_row, 'Diem phe binh'] = 29
df.loc[art_of_love_row, 'Cam xuc phe binh'] = 'positive'
df.loc[Samaritan, 'Ngay ra rap'] = 'Jul 5, 2022, Limited'

# Chuyển đổi cột "Ngay ra rap" thành định dạng dd/mm/yyyy.
df['Ngay ra rap'] = pd.to_datetime(df['Ngay ra rap'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0], format='%b %d, %Y', errors='coerce').dt.strftime('%d/%m/%Y')

# Chuyển đổi cột "Ngày phat song" với định dạng tương tự.
df['Ngay phat song'] = pd.to_datetime(df['Ngay phat song'].str.extract(r'(\d{1,2}-\w{3}-\d{2})')[0], format='%d-%b-%y', errors='coerce').dt.strftime('%d/%m/%Y')

# Hoán đổi cột 'ngày ra rạp' và 'ngày phát sóng'.
# Chọn hai cột để hoán đổi theo chỉ số.
col1 = 'Nam san xuat'       # Tên cột thứ nhất
col2 = 'Ten phim'     # Tên cột thứ hai

# Hoán đổi cột
df[[col1, col2]] = df[[col2, col1]]

# Cập nhật lại header ban đầu (sau khi đổi).
df.columns = [
    'Ma phim', 'Ten phim', 'Nguon xem phim', 'Nam san xuat', 
    'Diem phe binh', 'Cam xuc phe binh', 'Diem khan gia', 
    'Cam xuc cua khan gia', 'Ngay ra rap', 'Ngay phat song', 
    'Danh gia', 'Ngon ngu', 'Thoi luong phim'
]

print("-----------------------------------------------------------------")

# DELETE
# Loại bỏ các dòng có giá trị "null".
df = df.dropna()

# Xóa cột không cần thiết để có góc nhìn rõ hơn cho việc phân tích.
df = df.drop(columns=['Ma phim','Nguon xem phim'])

# Tương tự với xóa dòng.
# Cụ thể là xóa dòng 1 và 2 trong file.csv
df = df.drop(index=[0, 1])  

# Xóa dữ liệu có điều kiện.
df = df[df['Diem khan gia'] >= 20]

# Xóa dữ liệu bị trùng lặp (nếu có).
df = df.drop_duplicates()

#Lưu lại DataFrame đã được cập nhật vào một file CSV mới.
df.to_csv('newFileCrudData.csv', index=False)
print("File newFileCrudData.csv đã được tạo từ các thao tác CRUD (create, read, update, delete)")
print("-----------------------------------------------------------------")
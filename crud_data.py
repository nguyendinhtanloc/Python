import pandas as pd
import datetime

# <READ>
# Đọc dữ liệu từ file 'tmdb-movies.csv'.
df = pd.read_csv('tmdb-movies.csv')

print("----------------------------------------------------------------------------------")

# <CREATE>
# Thêm minh họa 3 dữ liệu mới vào file tmdb-movies.csv có sẵn.
# Dữ liệu 1: Tên phim 'Dragon Ball Z'
new_data1 = pd.DataFrame({
    'id': [132414],
    'imdb_id': ['tt105402'],
    'popularity': [44.565452],
    'budget': ['2.5E+08'],
    'revenue': ['2.8E+09'],
    'original_title': ['Dragon Ball Z'],
    'cast': ['Kakarot|Vegeta|Gogeta|Vegito|Broly|Son Gohan|Son Goten'],
    'homepage': ['https://dragonballwiki.net/xemphim/'],
    'director': ['Toriyama Akira'],
    'tagline': ['The power to protect the universe!'],
    'keywords': ['Saiyan|Kamehameha|Dragon Balls|Goku|Vegeta|Tournament|Super Saiyan|Adventure'],
    'overview': ['Several years after the defeat of powerful foes, peace has returned to Earth, but new threats arise as Goku and his friends train to protect their world from intergalactic dangers.'],
    'runtime': [154],
    'genres': ['Action|Adventure|Fantasy|Martial Arts'],
    'production_companies': ['Toei Animation'],
    'release_date': ['29/1/2024'],
    'vote_count': [5878],
    'vote_average': [6.8],
    'release_year': [2024],
    'budget_adj': ['2.34E+08'],
    'revenue_adj': ['2.35E+09'],
}) 

# Dữ liệu 2: Tên phim 'Detective Conan'
new_data2 = pd.DataFrame({
    'id': [132415],
    'imdb_id': ['tt105403'],
    'popularity': [53.857679],
    'budget': ['3E+0.8'],
    'revenue': ['3.7E+09'],
    'original_title': ['Detective Conan'],
    'cast': ['Kudo Shinichi|Yasaku Kudo|Yukiko Kudo|Ran Mori|Kogoro Mori|Kaito Kid|Haibara Ai'],
    'homepage': ['https://motchill.cafe/thong-tin-phim/conan-movie-27-100-man-dollar-no-michishirube.html'],
    'director': ['Aoyama Gosho'],
    'tagline': ['The truth never lies'],
    'keywords': ['Shinichi Kudo|Conan Edogawa|Mystery|Detective|Case|Black Organization|Evidence|Logic'],
    'overview': ['Years after becoming a child due to a mysterious poison, former teenage detective Shinichi Kudo, now Conan Edogawa, continues to solve intricate cases while pursuing the shadowy organization that transformed him.'],
    'runtime': [134],
    'genres': ['Mystery|Crime|Action|Drama'],
    'production_companies': ['TMS Entertainment'],
    'release_date': ['24/4/2024'],
    'vote_count': [5335],
    'vote_average': [6.7],
    'release_year': [2024],
    'budget_adj': ['1.87E+08'],
    'revenue_adj': ['1.89E+09'],
}) 

# Dữ liệu 3: Tên phim 'Doraemon'
new_data3 = pd.DataFrame({
    'id': [132416],
    'imdb_id': ['tt105404'],
    'popularity': [38.644869],
    'budget': ['1.8E+0.8'],
    'revenue': ['4.5E+09'],
    'original_title': ['Doraemon'],
    'cast': ['Nobita|Dorami|Doraemon|Suneo|Jaian|Shizuka'],
    'homepage': ['https://www.facebook.com/watch/?v=1597618247806044'],
    'director': ['Fujiko F. Fujio'],
    'tagline': ['The future is now!'],
    'keywords': ['Nobita|Time Machine|Gadgets|Friendship|Future|Cat Robot|Adventure|Problem Solving'],
    'overview': ['Many years after receiving a time machine, robotic cat Doraemon helps young Nobita navigate lifes challenges, using futuristic gadgets to improve his future and teach him important life lessons.'],
    'runtime': [123],
    'genres': ['Comedy|Adventure|Family|Science Fiction'],
    'production_companies': ['Shin-Ei Animation'],
    'release_date': ['15/10/2024'],
    'vote_count': [7785],
    'vote_average': [7.8],
    'release_year': [2024],
    'budget_adj': ['2.67E+08'],
    'revenue_adj': ['2.87E+09'],
}) 

# Kết hợp dữ liệu mới.
df = pd.concat([df, new_data1, new_data2, new_data3], ignore_index=True)

# Cập nhật lại vào file.csv (movies.csv)
# df.to_csv('NewTmdbMovies.csv', index=False)
print("file NewTmdbMovies.csv mới đã được tạo trên thao tác create data mới vào tmdb-movies.csv đã có sẵn.")

# Kiểm tra số lượng cột và in danh sách tên cột. 
print(len(df.columns))  # In ra số lượng cột
print(df.columns.tolist())  # In ra danh sách tên cột

print("----------------------------------------------------------------------------------")

# <UPDATE>
# Đổi header sang tiếng việt.
df.columns = [
    'Ma nhan dien', 'Dinh danh IMDb', 'Muc do pho bien', 'Ngan sach', 
    'Doanh thu', 'Tieu de goc', 'Dan dien vien', 'Trang chu', 'Dao dien', 
    'Khau hieu', 'Tu khoa', 'Tong quan', 'Thoi gian phat song', 'The loai', 
    'Cong ty san xuat', 'Ngay phat hanh', 'So phieu bau', 'So phieu bau trung binh', 
    'Nam phat hanh', 'Dieu chinh ngan sach', 'Dieu chinh doanh thu'
] 

# Đổi một số dữ liệu ở dòng 8 (cụ thể từ cột có 'Ma nhan dien: 87101',.....).
df.loc[df['Tieu de goc'] == 'Terminator Genisys', 'Tieu de goc'] = 'One Piece'
df.loc[(df['Ma nhan dien'] == 87101) & (df['Tieu de goc'] == 'One Piece'), 'Ma nhan dien'] = 135398
df.loc[(df['Dinh danh IMDb'] == 'tt1340138') & (df['Tieu de goc'] == 'One Piece'), 'Dinh danh IMDb'] = 'tt1234567'
df.loc[(df['Muc do pho bien'] == 8.654359) & (df['Tieu de goc'] == 'One Piece') , 'Muc do pho bien'] = 32.985763
df.loc[(df['Dan dien vien'] == 'Arnold Schwarzenegger|Jason Clarke|Emilia Clarke|Jai Courtney|J.K. Simmons') & (df['Tieu de goc'] == 'One Piece'), 'Dan dien vien'] = 'Shanks|Luffy|Zoro|Nami|Sanji'
df.loc[(df['Trang chu'] == 'http://www.terminatormovie.com/') & (df['Tieu de goc'] == 'One Piece'), 'Trang chu'] = 'http://www.onepiece.com/'
df.loc[(df['Dao dien'] == 'Alan Taylor') & (df['Tieu de goc'] == 'One Piece'), 'Dao dien'] = 'Emma Roberts'
df.loc[(df['Khau hieu'] == 'Reset the future') & (df['Tieu de goc'] == 'One Piece'), 'Khau hieu'] = 'Conquering a new ocean'
df.loc[(df['Tu khoa'] == 'saving the world|artificial intelligence|cyborg|killer robot|future') & (df['Tieu de goc'] == 'One Piece'), 'Tu khoa'] = 'anime|pirate|treasure|adventure|friendship'
df.loc[(df['Cong ty san xuat'] == 'Paramount Pictures|Skydance Productions') & (df['Tieu de goc'] == 'One Piece'), 'Cong ty san xuat'] = 'Toei Animation | Shueisha | Netflix'
df.loc[(df['Ngay phat hanh'] == '23/06/2015') & (df['Tieu de goc'] == 'One Piece'), 'Ngay phat hanh'] = '28/06/2025'
df.loc[(df['So phieu bau'] == 2598) & (df['Tieu de goc'] == 'One Piece'), 'So phieu bau'] = 5563
df.loc[(df['So phieu bau trung binh'] == 5.8) & (df['Tieu de goc'] == 'One Piece'), 'So phieu bau trung binh'] = 8.5

# Hoán đổi cột 'Muc do pho bien' và 'Tieu de goc' để có cái nhìn khách quan hơn.
col1 = 'Muc do pho bien'     # Tên cột thứ nhất
col2 = 'Tieu de goc'         # Tên cột thứ hai
df[[col1, col2]] = df[[col2, col1]]

# Cập nhật lại header ban đầu (sau khi đổi).
df.columns = [
    'Ma nhan dien', 'Dinh danh IMDb', 'Tieu de goc', 'Ngan sach', 
    'Doanh thu', 'Muc do pho bien', 'Dan dien vien', 'Trang chu', 'Dao dien', 
    'Khau hieu', 'Tu khoa', 'Tong quan', 'Thoi gian phat song', 'The loai', 
    'Cong ty san xuat', 'Ngay phat hanh', 'So phieu bau', 'So phieu bau trung binh', 
    'Nam phat hanh', 'Dieu chinh ngan sach', 'Dieu chinh doanh thu'
]

print("----------------------------------------------------------------------------------")

# <DELETE>

# Xóa cột 'Trang chu' không cần thiết
df = df.drop(['Trang chu'], axis=1)

# Xóa dữ liệu trùng (dữ liệu bị trùng sẽ giữ lại hàng đầu tiên, các hàng dữ liệu trùng với hàng đầu tiên sẽ bị loại bỏ).
df = df.drop_duplicates(subset=['Tieu de goc', 'Dao dien'], keep='first')

# Ví dụ điền giá trị bị thiếu vào hàng/cột có giá trị (null).
# B1. Tìm vị trí (null) của dòng có tieu de goc 'Manglehorn', 'By the Sea' bị thiếu.
Mang_le_horn = df[df['Tieu de goc'] == 'Manglehorn'].index[0]
Sa_ma_ri_tan = df[df['Tieu de goc'] == 'By the Sea'].index[0]

# B2. Điền giá trị null bị thiếu.
df.loc[Mang_le_horn, 'Tu khoa'] = 'Manglehorn|Al Pacino|David Gordon Green|Drama|Connection'
df.loc[Sa_ma_ri_tan , 'Khau hieu'] = 'The greatest journey is the journey within.'

# Lưu lại DataFrame đã được cập nhật vào một file CSV mới.
df.to_csv('newFileCrudData.csv', index=False)
print("File newFileCrudData.csv đã được tạo từ các thao tác CRUD (create, read, update, delete)")
print("----------------------------------------------------------------------------------")
import pandas as pd
import time

class CRUDData:
    print("\n" + " " * 50 + "========= CRUD dữ liệu =========\n")

    # <READ>
    print("Bắt đầu đọc dữ liệu...")
    start_time = time.time()  # Đánh dấu thời gian bắt đầu

    # Đọc dữ liệu từ file 'tmdb-movies.csv'.
    df = pd.read_csv('Data/DataFile.csv')

    elapsed_time = time.time() - start_time  # Tính thời gian chạy
    print(f"Thời gian chạy READ: {elapsed_time:.4f} giây\n")

    # <CREATE>
    print("Bắt đầu tạo dữ liệu mới...")
    start_time = time.time()

    # Thêm dữ liệu minh họa
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

    # Kết hợp dữ liệu
    df = pd.concat([df, new_data1], ignore_index=True)

    elapsed_time = time.time() - start_time
    print(f"Thời gian chạy CREATE: {elapsed_time:.4f} giây\n")

    # <UPDATE>
    print("Bắt đầu cập nhật dữ liệu...")
    start_time = time.time()

    # Đổi header sang tiếng Việt
    df.columns = [
        'Mã nhận diện', 'Định danh IMDb', 'Tiêu đề gốc', 'Ngân sách', 
        'Doanh thu', 'Mức độ phổ biến', 'Dàn diễn viên', 'Trang chủ', 'Đạo diễn', 
        'Khẩu hiệu', 'Từ khóa', 'Tổng quan', 'Thời lượng phát sóng', 'Thể loại', 
        'Công ty sản xuất', 'Ngày phát hành', 'Số phiếu bầu', 'Số phiếu bầu trung bình', 
        'Năm phát hành', 'Điều chỉnh ngân sách', 'Điều chỉnh doanh thu'
    ] 

    elapsed_time = time.time() - start_time
    print(f"Thời gian chạy UPDATE: {elapsed_time:.4f} giây\n")

    # <DELETE>
    print("Bắt đầu xóa dữ liệu không cần thiết...")
    start_time = time.time()

    # Xóa cột 'Trang chủ'
    df = df.drop(['Trang chủ'], axis=1)

    elapsed_time = time.time() - start_time
    print(f"Thời gian chạy DELETE: {elapsed_time:.4f} giây\n")

    # Lưu lại kết quả
    df.to_csv('Data/CRUD_DataFile.csv', index=False)
    print("File CRUD_DataFile.csv đã được cập nhật thành công.")
    print("\n" + " " * 45 + "========= Kết thúc CRUD dữ liệu =========\n")
    print("-" * 120)

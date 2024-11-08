import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('newFileCrudData.csv')

# Kiểm tra dữ liệu gốc
print(df['Ngay phat hanh'].head())

# Chuyển đổi cột ngày tháng
df['Ngay phat hanh'] = pd.to_datetime(df['Ngay phat hanh'], errors='coerce', dayfirst=False)

# Chuyển đổi lại cột 'Ngay phat hanh' về định dạng dd/mm/yyyy
df['Ngay phat hanh'] = df['Ngay phat hanh'].dt.strftime('%d/%m/%Y')

# Kiểm tra lại dữ liệu sau khi chuyển đổi
print(df['Ngay phat hanh'].head())

#Thay thế NaN bằng giá trị 0
df['Doanh thu'] = pd.to_numeric(df['Doanh thu'], errors='coerce').fillna(0)
df['Ngan sach'] = pd.to_numeric(df['Ngan sach'], errors='coerce').fillna(0)
df['Dieu chinh doanh thu'] = pd.to_numeric(df['Dieu chinh doanh thu'], errors='coerce').fillna(0)
df['Dieu chinh ngan sach'] = pd.to_numeric(df['Dieu chinh ngan sach'], errors='coerce').fillna(0)

#Chuyển đổi các cột số thành định dạng có dấu phân cách hàng nghìn

df['Doanh thu'] = df['Doanh thu'].apply(lambda x: "{:,.0f}".format(x))
df['Ngan sach'] = df['Ngan sach'].apply(lambda x: "{:,.0f}".format(x))
df['Dieu chinh doanh thu'] = df['Dieu chinh doanh thu'].apply(lambda x: "{:,.0f}".format(x))
df['Dieu chinh ngan sach'] = df['Dieu chinh ngan sach'].apply(lambda x: "{:,.0f}".format(x))


# Sử dụng f-string để định dạng số với 2 chữ số sau dấu phẩy
df['Muc do pho bien'] = df['Muc do pho bien'].apply(lambda x: f"{x:.2f}")

print(df['Doanh thu'].head())
print(df['Muc do pho bien'].head())

# Lưu lại vào file CSV
df.to_csv('newFileCleanData.csv', index=False)

print("File newFileCleanData.csv đã được tạo.")
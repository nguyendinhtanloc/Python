import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('newFileCleanData.csv')

#1. Đếm số lượng phim theo năm phát hành
film_count_per_year = df['Nam phat hanh'].value_counts().sort_index()

plt.figure(figsize=(14, 7))
plt.plot(film_count_per_year.index, film_count_per_year.values, marker='o', color='purple')
plt.title('Số lượng phim phát hành theo thời gian', fontsize=14, fontweight='bold', color='darkblue')
plt.xlabel('Năm phát hành', fontsize=13, fontweight='bold', color='darkblue')
plt.ylabel('Số lượng phim', fontsize=13, fontweight='bold', color='darkblue')
plt.grid()
plt.savefig('soluongphimquacacnam.png')
plt.close()

#2. 5 công ty sản xuất phim nhiều nhất piechart
df['Cong ty san xuat'] = df['Cong ty san xuat'].fillna('Các công ty khác')

company_counts = df['Cong ty san xuat'].value_counts()

top_companies = company_counts.head(5)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(12, 8))

plt.pie(top_companies, 
        labels=top_companies.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors,   
        shadow=True, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': 'solid'}) 

plt.title('5 công ty sản xuất phim nhiều nhất thống kê từ 1960 đến 2024', fontsize=16, fontweight='bold', color='darkblue')

plt.legend(top_companies.index, title='Công ty sản xuất', loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)

plt.savefig('top5congty.png')
plt.close()

#3. Biểu đồ phân tán doanh thu, ngân sách và số phiếu bầu
df['Ngan sach'] = pd.to_numeric(df['Ngan sach'].astype(str).str.replace(',', ''), errors='coerce')
df['Doanh thu'] = pd.to_numeric(df['Doanh thu'].astype(str).str.replace(',', ''), errors='coerce')
df['So phieu bau'] = pd.to_numeric(df['So phieu bau'], errors='coerce')

sns.set_style('darkgrid')

df['Ngan sach'] = df['Ngan sach'] / 1_000_000  
df['Doanh thu'] = df['Doanh thu'] / 1_000_000 

ngan_sach = df['Ngan sach']
doanh_thu = df['Doanh thu']
so_phieu_bau = df['So phieu bau']

plt.figure(figsize=(10, 6))

scatter = plt.scatter(ngan_sach, doanh_thu, s=so_phieu_bau/12, c=so_phieu_bau, cmap='viridis', alpha=0.7)

plt.title('Mối quan hệ giữa Ngân sách và Doanh thu (Triệu USD)', fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel('Ngân sách (Triệu USD)', fontsize=12, fontweight='bold', color='darkblue')
plt.ylabel('Doanh thu (Triệu USD)', fontsize=12, fontweight='bold', color='darkblue')

cbar = plt.colorbar(scatter)
cbar.set_label('Số phiếu bầu', fontsize=12, fontweight='bold', color='darkblue')

# so_phieu_bau_range = [2000, 4000, 6000, 8000]
# for a in so_phieu_bau_range:
#     plt.scatter([], [], s=a/12, label=str(a)) 
# plt.legend( title='Số phiếu bầu')

plt.savefig('Bieudophantan.png')
plt.close()

#4. Top 10 thể loại phim được yêu thích nhất
plt.figure(figsize=(16,10))
df["The loai"].value_counts()[:10].plot(kind="barh", color="orange")
plt.title("Top 10 thể loại phim được yêu thích ",fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel('Số lượng', fontsize=12, fontweight='bold', color='darkblue')
plt.ylabel('Thể loại', fontsize=12, fontweight='bold', color='darkblue')
plt.savefig('Top10theloaiduocyeuthich.png')
plt.close()


#5. Top 6 đạo diễn hàng đầu trong top 6 thể loại được yêu thích
# Lấy top 6 thể loại phổ biến nhất
top_6_the_loai = df['The loai'].value_counts().head(6).index

# Tạo figure với 3 hàng và 2 cột
fig, axes = plt.subplots(3, 2, figsize=(20, 12))

# Vẽ biểu đồ cho từng thể loại
for i in range(6):
    row = i // 2
    col = i % 2
    
    loai = top_6_the_loai[i]
    frame = df[df['The loai'] == loai]
    
    top_6_dao_dien = frame['Dao dien'].value_counts().head(6).index
    
    # Tạo biểu đồ đếm số lượng phim cho từng đạo diễn
    sns.countplot(x='Dao dien', data=frame[frame['Dao dien'].isin(top_6_dao_dien)], ax=axes[row, col], palette='Set2')
    
    axes[row, col].set_title('Top 6 Đạo diễn trong thể loại: ' + loai, fontsize=12, fontweight='bold')
    axes[row, col].set_ylabel('Số lượng phim', fontsize=8, fontweight='bold')
    axes[row, col].set_xlabel('Đạo diễn', fontsize=8, fontweight='bold')

    axes[row, col].set_xticklabels(top_6_dao_dien, rotation=45, ha='right', fontsize=8)

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=1.0)

plt.savefig('top6daodien.png')
plt.close()

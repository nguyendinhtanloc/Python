import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time  # Thêm module time để tính toán thời gian chạy

class FundamentalAnalysis:

    def __init__(self, file_path):
        # Đọc dữ liệu từ file CSV
        self.df = pd.read_csv(file_path, encoding='utf-8')
        print(f"Đã tải dữ liệu từ: {file_path}\n")
    
    def descriptive_statistics(self):
        # Thống kê mô tả cho các cột số
        description = self.df.describe()
        print("Thống kê mô tả cho các cột số:\n", description)
        return description
    
    def bivariate_analysis(self):
        start_time = time.time()  # Ghi lại thời gian bắt đầu

        # Phân tích phối hợp (Biến Độc lập vs Biến phụ thuộc)
        
        # Vẽ biểu đồ phân tán giữa 'Ngân sách' và 'Doanh thu'
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=self.df, x='Ngân sách', y='Doanh thu')
        plt.title('Biểu đồ phân tán giữa Ngân sách và Doanh thu')
        plt.xlabel('Ngân sách')
        plt.ylabel('Doanh thu')

        end_time = time.time()  # Ghi lại thời gian kết thúc
        execution_time = end_time - start_time  # Tính thời gian chạy
        print(f"\nThời gian thực thi biểu đồ phân tán \"Ngân sách\" và \"Doanh thu\": {execution_time:.2f} giây.")

        plt.show()

        start_time = time.time()  # Ghi lại thời gian bắt đầu

        # Vẽ biểu đồ pairplot giữa các cột số
        numeric_columns = ['Độ phổ biến', 'Ngân sách', 'Doanh thu', 'Thời lượng', 
                           'Số lượt bình chọn', 'Điểm trung bình', 'Ngân sách điều chỉnh', 'Doanh thu điều chỉnh']
        sns.pairplot(self.df[numeric_columns])
        plt.suptitle('Pairplot giữa các cột số', y=1.02)

        end_time = time.time()  # Ghi lại thời gian kết thúc
        execution_time = end_time - start_time  # Tính thời gian chạy
        print(f"\nThời gian thực thi phân tích biểu đồ \"Pariplot\" giữa các cột: {execution_time:.2f} giây.")
        print("Thời gian chạy có thể dài nhưng tổng cộng có 64 biểu đồ nên suy ra thao tác vẽ 1 biểu đồ < 1s")
        
        plt.show()
    
    def correlation_analysis(self):
        start_time = time.time()  # Ghi lại thời gian bắt đầu

        # Tính toán ma trận tương quan
        numeric_columns = ['Độ phổ biến', 'Ngân sách', 'Doanh thu', 'Thời lượng', 
                           'Số lượt bình chọn', 'Điểm trung bình', 'Ngân sách điều chỉnh', 'Doanh thu điều chỉnh']
        correlation_matrix = self.df[numeric_columns].corr()
        
        # In ma trận tương quan
        print("\nMa trận tương quan:\n", correlation_matrix)
        
        # Vẽ biểu đồ heatmap để hiển thị mối tương quan
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title('Ma trận tương quan giữa các cột số')

        end_time = time.time()  # Ghi lại thời gian kết thúc
        execution_time = end_time - start_time  # Tính thời gian chạy
        print(f"\nThời gian thực thi phân tích tương quan: {execution_time:.2f} giây.\n")

        plt.show()

def main():
    print(" " * 48 + "========= Phân tích cơ bản =========\n")
    
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Đảm bảo rằng bạn thay đổi đường dẫn đúng tới file dữ liệu của mình
    file_path = 'Data/Cleaned_DataFile.csv'  # Đường dẫn tới file CSV của bạn
    analysis = FundamentalAnalysis(file_path)

    # Thực hiện thống kê mô tả
    analysis.descriptive_statistics()
    
    end_time = time.time()  # Ghi lại thời gian kết thúc
    execution_time = end_time - start_time  # Tính thời gian chạy
    print(f"\nThời gian thực thi thống kê mô tả: {execution_time:.2f} giây.")

    # Thực hiện phân tích phối hợp
    analysis.bivariate_analysis()

    # Thực hiện phân tích tương quan
    analysis.correlation_analysis()
    
    print(" " * 44 + "========= Kết thúc phân tích cơ bản =========\n")
    print('-' * 120 + '\n')

if __name__ == "__main__":
    main()

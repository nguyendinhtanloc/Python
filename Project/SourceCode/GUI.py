import time
from tkinter import *
from tkinter.ttk import Combobox, Treeview, Notebook, Button, Style
import pandas as pd
import math


class GUI:
    print("\n" + " " * 48 + "========= Giao diện GUI =========\n")

    def __init__(self, master):     
        self.master = master
        self.master.title("Hệ thống quản lý dữ liệu phim")
        self.master.geometry("1024x768")  # Set a default size for the main window

        # Đọc dữ liệu từ file CSV
        try:
            self.df = pd.read_csv('Data/Cleaned_DataFile.csv')
        except FileNotFoundError:
            print("File CSV không tồn tại. Vui lòng kiểm tra đường dẫn và thử lại.")
            self.df = pd.DataFrame()

        # Tạo style cho các nút
        style = Style()
        style.configure("Custom.TButton",
                        background="#4CAF50",      # Màu nền
                        foreground="black",        # Màu chữ
                        font=("Arial", 12),
                        padding=10)
        style.map("Custom.TButton",
                background=[("active", "#45a049")])  # Màu khi nhấn

        # Nút để xem dữ liệu
        btn_view_data = Button(master, text="Xem dữ liệu", command=self.xemDuLieu, style="Custom.TButton")
        btn_view_data.pack(pady=20)

        # Nút "Thoát"
        btn_exit = Button(master, text="Thoát", command=self.master.quit, style="Custom.TButton")
        btn_exit.pack(pady=20)

    @staticmethod
    def search_data(column, value, data):
        if column == "Tất cả" or value == "Tất cả":
            df_filtered = data
        elif column and value:
            df_filtered = data[data[column].astype(str).str.contains(value, case=False, na=False)]
        elif column:
            df_filtered = data[[column]]
        else:
            df_filtered = data
        return df_filtered

    @staticmethod
    def sort_data(column, data, reverse=False):
        if column:
            df_sorted = data.sort_values(by=column, ascending=not reverse)
            return df_sorted
        return data

    @staticmethod
    def paginate_data(data, page, rows_per_page=50):
        total_rows = len(data)
        total_pages = math.ceil(total_rows / rows_per_page)
        start_idx = (page - 1) * rows_per_page
        end_idx = start_idx + rows_per_page
        paginated_data = data.iloc[start_idx:end_idx]
        return paginated_data, total_pages

    def xemDuLieu(self):
        if self.df.empty:
            print("Không có dữ liệu để hiển thị.")
            return

        # Tạo cửa sổ con để hiển thị dữ liệu
        new_window = Toplevel(self.master)
        new_window.title("Xem dữ liệu trước khi lọc")
        new_window.geometry("1024x768")  # Set a default size for the window
        new_window.config(bg="#f4f6f7")  # New background color for better contrast

        label_title = Label(new_window, text="Dữ liệu phim từ năm", font=("Arial", 18, 'bold'), bg="#f4f6f7", fg="#333333")
        label_title.pack(pady=20)

        # Tabs cho nội dung
        notebook = Notebook(new_window)
        notebook.pack(fill=BOTH, expand=True, pady=10)

        # Tạo tab dữ liệu chính
        tab_data = Frame(notebook, bg="#f9f9f9")
        notebook.add(tab_data, text="Dữ liệu")

        frame_new_buttons = Frame(tab_data, bg="#f9f9f9")
        frame_new_buttons.pack(pady=10)

        label_column = Label(frame_new_buttons, text="Chọn cột:", bg="#f9f9f9", fg="#000000", font=("Arial", 12))
        label_column.grid(row=0, column=0, padx=10, pady=10)

        combo_columns = Combobox(frame_new_buttons, values=["Tất cả"] + list(self.df.columns), font=("Arial", 12))
        combo_columns.grid(row=0, column=1, padx=10, pady=10)

        label_value = Label(frame_new_buttons, text="Nhập giá trị:", bg="#f9f9f9", fg="#000000", font=("Arial", 12))
        label_value.grid(row=0, column=2, padx=10, pady=10)

        combo_values = Combobox(frame_new_buttons, font=("Arial", 12))
        combo_values.grid(row=0, column=3, padx=10, pady=10)

        def update_values(event):
            column = combo_columns.get()
            if column and column != "Tất cả":
                unique_values = self.df[column].dropna().unique().tolist()
                combo_values['values'] = ["Tất cả"] + unique_values
            else:
                combo_values['values'] = ["Tất cả"]

        combo_columns.bind("<<ComboboxSelected>>", update_values)

        # Biến để lưu trữ dữ liệu hiện tại và trang hiện tại
        current_data = self.df
        current_page = 1

        # Frame chứa nội dung dữ liệu
        frame_new_content = Frame(tab_data, bg="#f9f9f9")
        frame_new_content.pack(fill=BOTH, expand=True)

        # Treeview với thanh cuộn ngang và dọc
        tree = Treeview(frame_new_content, columns=list(self.df.columns), show="headings", style="Treeview")
        for col in self.df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=CENTER)

        # Thanh cuộn ngang
        scroll_x = Scrollbar(frame_new_content, orient=HORIZONTAL, command=tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)
        tree.configure(xscrollcommand=scroll_x.set)

        # Thanh cuộn dọc
        scroll_y = Scrollbar(frame_new_content, orient=VERTICAL, command=tree.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scroll_y.set)

        tree.pack(side=LEFT, fill=BOTH, expand=True)

        # Frame chứa nút điều hướng trang
        frame_pagination = Frame(tab_data, bg="#f9f9f9")
        frame_pagination.pack(pady=10)

        label_page = Label(frame_pagination, text="")
        label_page.pack()

        def update_page_label(current_page, total_pages):
            label_page.config(text=f"Trang {current_page}/{total_pages}")

        def load_data(data):
            tree.delete(*tree.get_children())
            for index, row in data.iterrows():
                tree.insert("", "end", values=list(row))

        def change_page(direction, specific_page=None):
            nonlocal current_page, current_data
            if specific_page is not None:
                current_page = specific_page  # Chuyển trực tiếp đến trang cụ thể
            else:
                current_page += direction  # Thay đổi theo hướng

            paginated_data, total_pages = GUI.paginate_data(current_data, current_page)

            # Giới hạn trang trong phạm vi hợp lệ
            current_page = max(1, min(current_page, total_pages))
            load_data(paginated_data)
            update_page_label(current_page, total_pages)

        # Nút "Trang đầu"
        btn_first = Button(frame_pagination, text="Trang đầu", command=lambda: change_page(0, specific_page=1))
        btn_first.pack(side=LEFT, padx=5)

        # Nút "Trang trước"
        btn_prev = Button(frame_pagination, text="Trang trước", command=lambda: change_page(-1))
        btn_prev.pack(side=LEFT, padx=5)

        # Nút "Trang tiếp"
        btn_next = Button(frame_pagination, text="Trang tiếp", command=lambda: change_page(1))
        btn_next.pack(side=LEFT, padx=5)

        # Nút "Trang cuối"
        btn_last = Button(frame_pagination, text="Trang cuối", command=lambda: change_page(0, specific_page=total_pages))
        btn_last.pack(side=LEFT, padx=5)


        # Tạo một Frame riêng cho nút "Quay lại"
        frame_return = Frame(tab_data, bg="#f9f9f9")
        frame_return.pack(pady=10, fill=X)  # Đảm bảo frame chiếm hết chiều rộng

        # Nút "Quay lại"
        btn_return = Button(frame_return, text="Quay lại", command=new_window.destroy, style="Custom.TButton")
        btn_return.pack(side=RIGHT, padx=5)

        def search_and_paginate():
            nonlocal current_data, current_page
            current_data = GUI.search_data(combo_columns.get(), combo_values.get(), self.df)
            current_page = 1
            paginated_data, total_pages = GUI.paginate_data(current_data, current_page)
            load_data(paginated_data)
            update_page_label(current_page, total_pages)

        # Nút tìm kiếm
        btn_search = Button(frame_new_buttons, text="Tìm kiếm", command=search_and_paginate, style="Custom.TButton")
        btn_search.grid(row=0, column=4, padx=10, pady=10)

        # Load dữ liệu ban đầu
        load_data(current_data)
        paginated_data, total_pages = GUI.paginate_data(current_data, current_page)
        update_page_label(current_page, total_pages)


def main():
    start_time = time.time()  # Record the start time

    root = Tk()
    app = GUI(root)

    end_time = time.time()  # Record the end time

    root.mainloop()

    
    execution_time = end_time - start_time
    print(f"Thời gian thực thi: {execution_time:.2f} giây")

    print("\n" + " " * 44 + "========= Kết thúc giao diện GUI =========\n")
    print('\n' + '-' * 120 + '\n')

if __name__ == "__main__":
    main()

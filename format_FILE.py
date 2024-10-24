import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.styles import Alignment

os.system('cls')

df = pd.read_csv('filmCleaned.csv')

with pd.ExcelWriter('format_FilmCleaned.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    worksheet = writer.sheets['Sheet1']
    
    col_widths = {'A': 20, 'B': 30, 'C': 40, 'D': 15, 'E': 20, 'F': 20, 'G': 15, 'H': 25, 'I': 15}
    
    for col_letter, col_width in col_widths.items():
        worksheet.column_dimensions[col_letter].width = col_width
        
        cell = worksheet['{}1'.format(col_letter)]
        cell.alignment = Alignment(horizontal='center')
        
        for cell in worksheet[col_letter][1:]:
            if col_letter in ['A', 'D', 'E', 'F', 'G', 'H']:
                cell.alignment = Alignment(horizontal='center')
            elif col_letter in ['B', 'C']:
                cell.alignment = Alignment(horizontal='left')

print("File format_FilmCleaned.xlsx đã được tạo.")

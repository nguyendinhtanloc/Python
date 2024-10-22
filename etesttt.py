import pandas as pd
import os
os.system('cls')

df = pd.read_csv('movies.csv')
# print(df.columns.str.title()) 
df = df.drop('movieId', axis = 1)
df = df.drop('critic_sentiment', axis = 1)
df = df.drop('audience_sentiment', axis = 1)
df = df.drop('audience_score', axis = 1)
print(df)
df.columns = ['Nam san xuat','Nguon xem phim','Ten phim','Diem phe binh (100/100)','Ngay ra rap','Ngay phat song','Danh gia','Ngon ngu','Thoi luong phim']

# df.rename(colunms = {'movieYear':'Nam san xuat',
#                      'movieURL':'Nguon xem phim',
#                       'movieTitle':'Ten phim',
#                        'critic_score':'Diem (100/100)',
#                         'release_date_theaters':'Ngay ra rap',
#                         'release_date_streaming':'Ngay phat hanh truc tuyen'}, inplace = True)
print(df.head())
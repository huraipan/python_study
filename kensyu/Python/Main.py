import requests
from bs4 import BeautifulSoup
import traceback
import pandas as pd
import datetime
import os
import logging
import sys
import matplotlib.pyplot as plt



logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler('./my.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)



args = sys.argv
code = args[1]
year, month, day = map(int, args[2].split('-'))


url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
soap = BeautifulSoup(res.text, 'lxml')
el_table_navi = soap.find("table", class_="Nnavi")
el_td_last = el_table_navi.find("td", class_="pgRR")
pg_last = el_td_last.a.get('href').rsplit('&')[1]
pg_last = pg_last.split('=')[1]
pg_last = int(pg_last)

def parse_page(code, page):
    try:
        url = 'http://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'.format(code=code, page=page)
        res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        _soap = BeautifulSoup(res.text, 'lxml')
        _df = pd.read_html(str(_soap.find("table")), header=0)[0]
        _df = _df[['날짜','종가', '거래량']].dropna(how="all")
        return _df
    except Exception as e:
        traceback.print_exc()
    return None


str_datefrom = datetime.datetime.strftime(datetime.datetime(year=year, month=month, day=day), '%Y.%m.%d')
str_dateto = datetime.datetime.strftime(datetime.datetime.today(), '%Y.%m.%d')


df = None
for page in range(1, pg_last + 1):
    _df = parse_page(code, page)
    _df_filtered = _df[_df['날짜'] > str_datefrom]
    if df is None:
         df = _df_filtered
    else:
           df = pd.concat([df, _df_filtered])
    if len(_df) > len(_df_filtered):
          break






df = df.rename(columns={'날짜': 'date', '종가': 'close', '거래량': 'volume'})




path_dir = './data'
if not os.path.exists(path_dir):
    os.makedirs(path_dir)
path = os.path.join(path_dir, '{code}_{date_from}_{date_to}.csv'.format(code=code, date_from=str_datefrom,
                                                                        date_to=str_dateto))
df.to_csv(path, index=False)





folderPath = r'./data'
attributeTable = '005930_2023.01.01_2023.03.08.csv'
os.chdir(folderPath)
df = pd.read_csv(attributeTable)

df = df[['date', 'close', 'volume']]
fig, ax1 = plt.subplots()
color_1 = 'tab:blue'
ax1.set_title('close and volume', fontsize=10)
ax1.set_xlabel('Date')
ax1.set_ylabel('close', fontsize=10, color=color_1)
ax1.plot(df.date, df.close, marker='s', color=color_1)
ax1.tick_params(axis='y', labelcolor=color_1)

ax2 = ax1.twinx()
color_2 = 'tab:red'
ax2.set_ylabel('volume', fontsize=10, color=color_2)
ax2.plot(df.date, df.volume, marker='o', color=color_2)
ax2.tick_params(axis='y', labelcolor=color_2)

fig.tight_layout()

plt.show()



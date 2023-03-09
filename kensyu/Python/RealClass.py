import requests
from bs4 import BeautifulSoup
import traceback
import pandas as pd
import datetime
import os
import logging
import matplotlib.pyplot as plt




class Stock:
    def __init__(self, code, year, month, day):
        self.code = code
        self.year = year
        self.month = month
        self.day = day

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
    def run(self):

        Stock.crawling(self)
        Stock.graph(self)



    def crawling(self):
        code = self.code
        year = self.year
        month = self.month
        day = self.day

        try:
            url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
            res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
            soap = BeautifulSoup(res.text, 'lxml')
            el_table_navi = soap.find("table", class_="Nnavi")
            el_td_last = el_table_navi.find("td", class_="pgRR")
            pg_last = el_td_last.a.get('href').rsplit('&')[1]
            pg_last = pg_last.split('=')[1]
            pg_last = int(pg_last)
        except Exception:
            print("please input right code")
            self.logger.warning("input wrong code")

        def parse_page(code, page):
            try:
                url = 'http://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'.format(code=code, page=page)
                res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
                _soap = BeautifulSoup(res.text, 'lxml')
                _df = pd.read_html(str(_soap.find("table")), header=0)[0]
                _df = _df[['날짜', '종가', '거래량']].dropna(how="all")
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


    def graph(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Read the CSV file
        df = pd.read_csv('./data/005930_2023.01.01_2023.03.08.csv')

        # Clean and transform the data
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df.sort_index(inplace=True)

        # Create the plot
        sns.set_style('darkgrid')
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Plot the closing prices on the first y-axis
        ax1.plot(df['close'], label='Closing Price')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price')

        # Create a second y-axis for the trading volume
        ax2 = ax1.twinx()
        ax2.plot(df['volume'], color='orange', label='Trading Volume')
        ax2.set_ylabel('Volume')

        # Set the x-ticks
        num_ticks = 10  # Set the number of tick marks
        xtick_labels = [df.index[i].strftime('%Y-%m-%d') for i in range(0, len(df), len(df) // num_ticks)]
        xtick_positions = [df.index[i] for i in range(0, len(df), len(df) // num_ticks)]
        ax1.set_xticks(xtick_positions)
        ax1.set_xticklabels(xtick_labels, rotation=90)

        # Adjust the plot size and padding of the x-tick labels
        plt.subplots_adjust(bottom=0.2)

        # Show the legend
        fig.legend(loc='upper right', bbox_to_anchor=(0.88, 0.85))

        # Set the title
        plt.title('Stock Closing Prices and Trading Volumes')

        # Show the plot
        plt.show()




    

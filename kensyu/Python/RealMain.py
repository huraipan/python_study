import argparse
from RealClass import Stock
import FinanceDataReader as fdr





def by_name(item_name):
    df_krx = fdr.StockListing('KRX')
    item_code_list = df_krx.loc[df_krx["Name"] == item_name, "Code"].tolist()
    if len(item_code_list) > 0:
        item_code = item_code_list[0]
        return item_code
    else:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('code', type=str, help="code")
    parser.add_argument('date', type=str, help="date")

    args = parser.parse_args()

    if(by_name(args.code) == False):
        code = args.code
        try:
            year, month, day = map(int, args.date.split('-'))
        except Exception:
            print("please input like 2023-1-1")
            Stock.logger.warning("Unformatted Date")

        a = Stock(code, year, month, day)

        if __name__ == "__main__":
            a.run()

    else:
        code = by_name(args.code)
        try:
            year, month, day = map(int, args.date.split('-'))
        except Exception:
            print("please input like 2023-1-1")
            Stock.logger.warning("Unformatted Date")

        a = Stock(code, year, month, day)

        if __name__ == "__main__":
            a.run()







if __name__=="__main__":
    main()






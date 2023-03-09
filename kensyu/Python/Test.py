import FinanceDataReader as fdr


df_krx = fdr.StockListing('KRX')

item_name = "삼성전자"
code = df_krx.loc[df_krx["Name"] == item_name, "Code"].tolist()[0]
print(code)






def item_code_by_item_name(item_name):

    item_code_list = df_krx.loc[df_krx["Name"] == item_name, "Code"].tolist()
    if len(item_code_list) > 0:
        item_code = item_code_list[0]
        return item_code
    else:
        return False

import pandas as pd
def alphavantage_api_csv_download_raw(function, symbol, alpha_vantage_key):
    function = function
    symbol = symbol
    datatype = 'csv'

    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&datatype={datatype}&apikey={alpha_vantage_key}"
    return pd.read_csv(url)

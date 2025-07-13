import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_cik(ticker):
    url = f"https://www.sec.gov/files/company_tickers_exchange.json"
    headers = {"User-Agent": "YourName YourEmail@example.com"}
    r = requests.get(url, headers=headers)
    data = r.json()
    for item in data.values():
        if item['ticker'].lower() == ticker.lower():
            return str(item['cik_str']).zfill(10)
    raise ValueError("未找到对应CIK")

def get_latest_10k_url(cik):
    headers = {"User-Agent": "YourName YourEmail@example.com"}
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(url, headers=headers)
    data = r.json()
    for filing in data["filings"]["recent"]["form"]:
        if filing == "10-K":
            idx = data["filings"]["recent"]["form"].index(filing)
            acc_num = data["filings"]["recent"]["accessionNumber"][idx].replace("-", "")
            return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_num}/Financial_Report.xlsx"
    raise ValueError("未找到10-K文件")

def get_financial_data(ticker):
    cik = get_cik(ticker)
    url = get_latest_10k_url(cik)
    return pd.DataFrame([{"Ticker": ticker, "CIK": cik, "10-K链接": url}])

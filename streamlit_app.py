import streamlit as st
from utils.sec_parser import get_financial_data

st.set_page_config(page_title="SEC 财报提取 Agent", layout="wide")
st.title("📊 SEC 财务数据提取助手")

ticker = st.text_input("请输入美股代码（如 AAPL、GOOG）:")

if st.button("提取财报数据") and ticker:
    with st.spinner("正在从SEC下载财报，请稍候..."):
        try:
            data = get_financial_data(ticker)
            st.success("成功提取以下数据：")
            st.dataframe(data)
            st.download_button("下载为CSV", data.to_csv(index=False), file_name=f"{ticker}_financials.csv")
        except Exception as e:
            st.error(f"提取失败：{e}")

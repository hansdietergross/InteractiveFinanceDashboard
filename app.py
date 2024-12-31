import streamlit as st
import yfinance as yf
import pandas as pd

def relativeret (df):
    rel= df.pct_change()
    cumret = (1+rel).cumprod() - 1 
    cumret = cumret.fillna(0) 
    return cumret

#Set the page config at the beginning of your app script
st.set_page_config(
    page_title="My personal Finance Dashboard",
    layout="wide"
)

st.title('My personal Finance Dashboard')
tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD')
dropdown = st.multiselect('Pick your assets',tickers)
start = st.date_input('Start', value = pd.to_datetime('2021-01-01')) 
end = st.date_input('End', value = pd.to_datetime('today'))
if len(dropdown) > 0:    
    progress_bar = st.progress (0)
    for perc_completed in range(100):
        #time.sleep(0.2)
        progress_bar.progress (perc_completed+1)
    df = yf.download (dropdown, start, end) ['Adj Close'] 
    df = relativeret (df) 
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
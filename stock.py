import yfinance as yf
import streamlit as st
import pandas as pd
                                              


st.write("""
# simple stock price App

shown are the stock **closing price** and **volume** of Google!


                                                    
[Google](http://www.google.com)


""")

#difine the ticker symbole

tickerSymbol = "GOOGL"

#get data of this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical price forr this ticker
tickerDf = tickerData.history(period='id',start='2010-5-31',end='2020-5-31')
#open high low close volume dividends stock splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
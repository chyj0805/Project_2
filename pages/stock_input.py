from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.chart_container import chart_container
import extra_streamlit_components as stx
from markdownlit import mdlit
import pandas as pd
import datetime
import streamlit as st
import os
import hvplot.pandas
import time
import requests
from alpha_vantage.timeseries import TimeSeries

st.set_page_config(
    page_title="Sector Selection",
    page_icon="📊",
    layout="wide",
)

st.markdown("# Stock sector selection")
st.sidebar.header("Stock sector selection")
stock_symbol = ""
placeholder_for_selectbox = st.empty()
#setting tabs using extras
tab = stx.tab_bar(data=[
    stx.TabBarItemData(id="Sector Select", title="📈 Sector Select", description="Choose from three sectors"),
    stx.TabBarItemData(id="Manual Input", title="✅ Manual Input", description="Pick your own Symbol or Ticker")])
# dashboard title
option = st.selectbox(
            'Which sector would you like to focus on?',
            ('Energy', 'Tech', 'Financial'))

st.write('You selected:', option)

st.title("Sector Selection")
if tab == "Sector Select":
    with placeholder_for_selectbox:       
        if option == 'Energy':
            stock_symbol = str('IYE')
        elif option == 'Tech':
            stock_symbol = str('IYW')    
        else:
            stock_symbol = str('IYF')
    ts = TimeSeries(key='4FHTO2GAT3NL1EZ8', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=stock_symbol,interval='1min', outputsize='full')
    st.dataframe(data)
else:
        st.error("")

if tab == "Manual Input":
    stock_symbol = st.text_input("Enter your other option...")
    st.info(
        f":white_check_mark: The written option is **{stock_symbol}**")
else:
        st.error("")
if placeholder_for_selectbox is st.empty():
    n_years = st.empty()
else:
     st.write("thank you")
    # n_years = st.slider('Years of predicition:', 1 ,4)
    # ts = TimeSeries(key='4FHTO2GAT3NL1EZ8', output_format='pandas')
    # data, meta_data = ts.get_intraday(symbol=stock_symbol,interval='1min', outputsize='full')
    # st.dataframe(data)
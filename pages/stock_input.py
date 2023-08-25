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

st.set_page_config(
    page_title="Sector Selection",
    page_icon="📊",
    layout="wide",
)

st.markdown("# Stock sector selection")
st.sidebar.header("Stock sector selection")

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
    with st.form('Sector Select'):
        submit_button = st.form_submit_button("Submit!")
        placeholder_for_selectbox = st.empty()
        
        
        with placeholder_for_selectbox:       
            if option == 'Energy':
                energy_option = st.selectbox('Please choose one of the sample stocks ',
                                                ('XOM','CVX','ENB'))
            elif option == 'Tech':
                tech_option = st.selectbox('Please choose one of the sample stocks ',
                                                ('APPL','NVDA','AVGO'))    
            else:
                fin_option = st.selectbox('Please choose one of the sample stocks ',
                                                ('WFC','BAC','JPM'))
            
elif tab == "Manual Input":
    with st.form("Manual Input"):
        manual_submit_button = st.form_submit_button("Submit!")
    symbol = st.text_input("Enter your other option...")
    st.info(
        f":white_check_mark: The written option is **{symbol}**")
else:
        st.error("`st.form_submit_button` has not been clicked yet")
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.chart_container import chart_container
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

#@st.experimental_memo

# dashboard title
st.title("Sector Selection")

option = st.selectbox(
    'Which sector would you like to focus on?',
    ('Energy', 'Tech', 'Financial'))

st.write('You selected:', option)
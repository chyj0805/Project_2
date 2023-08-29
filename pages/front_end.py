
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
    page_title="Stock prediction",
    page_icon="📈",
    layout="wide",
)


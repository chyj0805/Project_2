
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
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor

st.set_page_config(
    page_title=" LSTM Model",
    page_icon="📈",
    layout="wide",
)

energy_data = {
    'Exxon Mobil Corporation': 'XOM',
    'Chevron Corporation': 'CVX',
    'Conoco Phillips': 'COP',
    'SLB': 'SLB',
    'EOG Resources, Inc.': 'EOG',
    'Marathon Petroleum Corporation': 'MPC',
    'Pioneer Natural Resources Company': 'PXD',
    'Phillips 66': 'PSX',
    'Valero Energy Corporation': 'VLO',
    'Occidental Petroleum Corporation': 'OXY',
    'Hess Corporation': 'HES',
    'Williams Cos Inc': 'WMB',
    'Cheniere Energy, Inc.': 'LNG',
    'Baker Hughes Company': 'BKR',
    'Halliburton Company': 'HAL',
    'Kinder Morgan, Inc.': 'KMI',
    'Devon Energy Corporation': 'DVN',
    'ONEOK, Inc.': 'OKE',
    'Diamondback Energy, Inc.': 'FANG',
    'Coterra Energy Inc.': 'CTRA',
    'First Solar, Inc.': 'FSLR',
    'Targa Resources Corp.': 'TRGP',
    'Enphase Energy, Inc.': 'ENPH',
    'Marathon Oil Corporation': 'MRO',
    'EQT Corporation': 'EQT',
    'APA Corporation': 'APA',
    'Ovintiv Inc.': 'OVV',
    'Texas Pacific Land Corporation': 'TPL',
    'Chesapeake Energy Corporation': 'CHK',
    'TechnipFMC plc': 'FTI',
    'NOV Inc.': 'NOV',
    'HF Sinclair Corporation': 'DINO',
    'Antero Resources Corporation': 'AR',
    'Range Resources Corporation': 'RRC',
    'Southwestern Energy Company': 'SWN',
    'USD CASH': 'USD',
    'DT Midstream, Inc.': 'DTM',
    'Plug Power Inc.': 'PLUG',
    'Antero Midstream Corporation': 'AM',
    'ChargePoint Holdings, Inc.': 'CHPT',
    'New Fortress Energy Inc.': 'NFE',
    'BLK CSH FND TREASURY SL AGENCY': 'XTSLA',
    'CASH COLLATERAL USD WFFUT': 'WFFUT',
    'EMINI ENERGY SELECT SECTOR SEP 23': 'IXPU3'
}

# Financial data dictionary
finn_data = {
    'Berkshire Hathaway Inc.': 'BRK-B',
    'JPMorgan Chase & Co.': 'JPM',
    'Bank of America Corporation': 'BAC',
    'Wells Fargo & Company': 'WFC',
    'S&P Global Inc.': 'SPGI',
    'The Goldman Sachs Group, Inc.': 'GS',
    'BlackRock, Inc.': 'BLK',
    'Morgan Stanley': 'MS',
    'Marsh & McLennan Companies, Inc.': 'MMC',
    'Charles Schwab Corp.': 'SCHW',
    'Chubb Limited': 'CB',
    'Citigroup Inc.': 'C',
    'The Progressive Corporation': 'PGR',
    'Blackstone Inc.': 'BX',
    'CME Group Inc.': 'CME',
    'Aon plc': 'AON',
    'Intercontinental Exchange, Inc.': 'ICE',
    'U.S. Bancorp': 'USB',
    'MOODYS CORP': 'MCO',
    'Arthur J. Gallagher & Co.': 'AJG',
    'The PNC Financial Services Group, Inc.': 'PNC',
    'Aflac Incorporated': 'AFL',
    'Apollo Global Management, Inc.': 'APO',
    'American International Group, Inc.': 'AIG',
    'MSCI Inc.': 'MSCI',
    'MetLife, Inc.': 'MET',
    'Truist Financial Corporation': 'TFC',
    'KKR & Co. Inc.': 'KKR',
    'Travelers Companies Inc.': 'TRV',
    'Ameriprise Financial, Inc.': 'AMP',
    'The Bank of New York Mellon Corporation': 'BK',
    'Prudential Financial, Inc.': 'PRU',
    'The Allstate Corporation': 'ALL',
    'Arch Capital Group Ltd.': 'ACGL',
    'T. Rowe Price Group, Inc.': 'TROW',
    'State Street Corporation': 'STT',
    'Discover Financial Services': 'DFS',
    'Willis Towers Watson PLC': 'WTW',
    'Hartford Financial Services Group Inc.': 'HIG',
    'Broadridge Financial Solutions, Inc.': 'BR',
    'M&T Bank Corporation': 'MTB',
    'Raymond James Financial, Inc.': 'RJF',
    'Markel Corporation': 'MKL',
    'Principal Financial Group, Inc.': 'PFG',
    'LPL Financial Holdings Inc.': 'LPLA',
    'Nasdaq, Inc.': 'NDAQ',
    'Fifth Third Bancorp': 'FITB',
    'Brown & Brown, Inc.': 'BRO',
    'Regions Financial Corporation': 'RF',
    'FactSet Research Systems Inc.': 'FDS'
}

# Technology data dictionary
tech_data = {
    'Apple Inc.': 'AAPL',
    'Microsoft Corporation': 'MSFT',
    'Alphabet Inc.': 'GOOGL',
    'NVIDIA Corporation': 'NVDA',
    'Alphabet Inc.': 'GOOG',
    'Meta Platforms, Inc.': 'META',
    'Broadcom Inc.': 'AVGO',
    'Adobe Inc.': 'ADBE',
    'Salesforce, Inc.': 'CRM',
    'Oracle Corporation': 'ORCL',
    'Advanced Micro Devices, Inc.': 'AMD',
    'Texas Instruments Incorporated': 'TXN',
    'Intuit Inc.': 'INTU',
    'Intel Corporation': 'INTC',
    'International Business Machines Corporation': 'IBM',
    'Applied Materials, Inc.': 'AMAT',
    'QUALCOMM Incorporated': 'QCOM',
    'ServiceNow, Inc.': 'NOW',
    'Lam Research Corporation': 'LRCX',
    'Analog Devices, Inc.': 'ADI',
    'Micron Technology, Inc.': 'MU',
    'Palo Alto Networks, Inc.': 'PANW',
    'Synopsys, Inc.': 'SNPS',
    'KLA Corporation': 'KLAC',
    'Cadence Design Systems, Inc.': 'CDNS',
    'Roper Technologies, Inc.': 'ROP',
    'Amphenol Corporation': 'APH',
    'Marvell Technology, Inc.': 'MRVL',
    'Workday, Inc.': 'WDAY',
    'Snowflake Inc.': 'SNOW',
    'Autodesk, Inc.': 'ADSK',
    'Microchip Technology Incorporated': 'MCHP',
    'ON Semiconductor Corporation': 'ON',
    'Fortinet, Inc.': 'FTNT',
    'Cognizant Technology Solutions Corporation': 'CTSH',
    'VMware, Inc.': 'VMW',
    'CrowdStrike Holdings, Inc.': 'CRWD',
    'Palantir Technologies Inc.': 'PLTR',
    'Atlassian Corporation Plc': 'TEAM',
    'CDW Corporation': 'CDW',
    'ANSYS, Inc.': 'ANSS',
    'Gartner, Inc.': 'IT',
    'Datadog, Inc.': 'DDOG',
    'HP Inc.': 'HPQ',
    'DoorDash, Inc.': 'DASH',
    'Corning Incorporated': 'GLW',
    'MongoDB, Inc.': 'MDB',
    'HubSpot, Inc.': 'HUBS',
    'Monolithic Power Systems, Inc.': 'MPWR',
    'Hewlett Packard Enterprise Company': 'HPE'
}
def main():
    st.title("LSTM Training")
# Dropdown to select a category
    selected_category = st.selectbox("Select a Category", ["Energy", "Financial", "Technology"])
   
    # Display the selected category's dropdown and ticker symbol
    if selected_category == "Energy":
        selected_company = st.selectbox("Select an Energy Company", list(energy_data.keys()))
        if selected_company in energy_data:
            ticker = energy_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker}")
            # Initialize the StockModelTrainerPredictor class with the selected ticker symbol
            predictor = StockModelTrainerPredictor(ticker)

        # Button to fetch and preprocess data for model training
        train_model_button = st.button("Fetch and Preprocess Data for Training")
        if train_model_button:
            with st.spinner("Fetching and preprocessing data for training..."):
                # Use the class method to fetch and preprocess data
                combined_data = predictor.preprocess_data()

                # Display the combined data as a DataFrame
                st.success("Data is ready for model training!")
                st.dataframe(combined_data)

                # Set data_is_ready to True when data is successfully fetched and preprocessed
                data_is_ready = True

                # Check if data is ready for model training
                if data_is_ready:
                    # Button to train the model
                    train_model_button = st.button("Train Model")

                if train_model_button:
                    # Call the train_model() method from your class
                    trained_model = predictor.train_model()

                    # Save the trained model as a .h5 file
                    model_filename = f"{selected_company}_model.h5"
                    trained_model.save(model_filename)

                    # Provide a link to download the model file
                    st.success("Model training complete! You can download the model below.")
                    st.markdown(f"**[Download Trained Model]({model_filename})**", unsafe_allow_html=True)
        else:
            st.write("Please select an energy company.")
   
    elif selected_category == "Financial":
        selected_company = st.selectbox("Select a Financial Company", list(finn_data.keys()))
        if selected_company in finn_data:
            ticker = finn_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker}")
            # Button to train the model
            train_button = st.button("Train Model")
            if train_button:
                st.write("Training the model...")
                predictor = StockModelTrainerPredictor(ticker)

            # Button to fetch and combine data for model training
            fetch_data_button = st.button("Fetch Data for Training")
            if fetch_data_button:
                with st.spinner("Fetching and combining data for training..."):
                    # Use the class method to fetch and combine data
                    combined_data = predictor.get_combined_data()
                    data_is_ready = True  # Set data_is_ready to True once data is ready
                # Display the combined data as a DataFrame
                st.success("Data is ready for model training!")
                st.dataframe(combined_data)

                # Check a condition to determine whether to show the training button
                if data_is_ready:
                    # Place the "Train Model" button next to the "Fetch Data for Training" button
                    col1, col2 = st.columns(2)
                    with col1:
                        # Button to train the model
                        train_model_button = st.button("Train Model")

                    if train_model_button:
                        # Call the train_model() method from your class
                        trained_model = predictor.train_model()

                        # Save the trained model as a .h5 file
                        model_filename = f"{selected_company}_model.h5"
                        trained_model.save(model_filename)

                        # Provide a link to download the model file
                        st.success("Model training complete! You can download the model below.")
                        st.markdown(f"**[Download Trained Model]({model_filename})**", unsafe_allow_html=True)
        else:
            st.write("Please select a financial company.") 
    elif selected_category == "Technology":
        selected_company = st.selectbox("Select a Technology Company", list(tech_data.keys()))
        if selected_company in tech_data:
            ticker = tech_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker}")
            predictor = StockModelTrainerPredictor(ticker)

            # Button to fetch and combine data for model training
            fetch_data_button = st.button("Fetch Data for Training")
            if fetch_data_button:
                with st.spinner("Fetching and combining data for training..."):
                    # Use the class method to fetch and combine data
                    combined_data = predictor.get_combined_data()
                    data_is_ready = True  # Set data_is_ready to True once data is ready
                # Display the combined data as a DataFrame
                st.success("Data is ready for model training!")
                st.dataframe(combined_data)

                # Check a condition to determine whether to show the training button
                if data_is_ready:
                    # Place the "Train Model" button next to the "Fetch Data for Training" button
                    col1, col2 = st.columns(2)
                    with col1:
                        # Button to train the model
                        train_model_button = st.button("Train Model")

                    if train_model_button:
                        # Call the train_model() method from your class
                        trained_model = predictor.train_model()

                        # Save the trained model as a .h5 file
                        model_filename = f"{selected_company}_model.h5"
                        trained_model.save(model_filename)

                        # Provide a link to download the model file
                        st.success("Model training complete! You can download the model below.")
                        st.markdown(f"**[Download Trained Model]({model_filename})**", unsafe_allow_html=True)
        else:
            st.write("Please select a technology company.")


if __name__ == "__main__":
    main()
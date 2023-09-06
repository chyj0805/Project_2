import streamlit as st
import os
import zipfile
import tempfile
import tensorflow as tf
import matplotlib.pyplot as plt  # You can use matplotlib for visualizations
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor

# Create a Streamlit app
st.title("Stock Prediction Model")

# Energy data dictionary
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

# Allow the user to upload the zipped model file
zip_file = st.file_uploader('TF.Keras model file (.h5py.zip)', type='zip')
selected_sector = st.sidebar.selectbox("Select a Sector", ["Energy", "Financial", "Technology"])
# Check if a valid sector is selected
if selected_sector:
    st.sidebar.write(f"Selected Sector: {selected_sector}")

    # Create a dictionary based on the selected sector
    if selected_sector == "Energy":
        selected_dict = energy_data
    elif selected_sector == "Financial":
        selected_dict = finn_data
    elif selected_sector == "Technology":
        selected_dict = tech_data
    else:
        selected_dict = {}

    # Select a company within the selected sector
    selected_company = st.sidebar.selectbox(f"Select a {selected_sector} Company", list(selected_dict.keys()))

predictor = None
data_is_ready = False
loaded_model = None
# Check if a valid company is selected
if selected_company:
    ticker_symbol = selected_dict[selected_company]
    st.sidebar.write(f"Ticker Symbol for {selected_company}: {ticker_symbol}")

    # Initialize predictor with the selected ticker symbol
predictor = StockModelTrainerPredictor(ticker_symbol)

load_model_button = st.button("Load Model")
if load_model_button and zip_file:
    with tempfile.TemporaryDirectory() as tmp_dir:
        with zipfile.ZipFile(zip_file, 'r') as myzipfile:
            myzipfile.extractall(tmp_dir)
            root_folder = myzipfile.namelist()[0]
            model_path = os.path.join(tmp_dir, root_folder)  # Full path to the model file
            
            st.info(f'Loading model from temporary directory: {model_path}')
            
            if os.path.exists(model_path) and model_path.endswith('.h5'):
                # Define custom metric function
                def root_mean_squared_error(y_true, y_pred):
                    return tf.sqrt(tf.reduce_mean(tf.square(y_pred - y_true), axis=-1))
                
                # Load the pre-trained model and specify the custom_objects dictionary
                loaded_model = tf.keras.models.load_model(model_path, custom_objects={'root_mean_squared_error': root_mean_squared_error})
                
                if loaded_model:
                    st.write(f"Model '{model_path}' loaded successfully.")
                    # Create a predictor with the loaded model
                    predictor = StockModelTrainerPredictor(loaded_model)  
                else:
                    st.error(f"Failed to load the model '{model_path}'.")
            else:
                st.error("No valid .h5 model file found in the extracted directory.")

# Button to make predictions with the selected model
predict_button = st.sidebar.button("Predict with Selected Model")
if predict_button:
    if predictor.model is not None:
        # If the model is loaded successfully, make predictions
        predictions = predictor.predict_with_pretrained_model()
        if predictions is not None:
            st.subheader("Predictions")
            st.write(predictions)
    else:
        st.error("No model is loaded. Cannot make predictions.")



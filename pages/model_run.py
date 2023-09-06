import streamlit as st
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor
import os
st.set_page_config(
    page_title="Stock Prediction",
    page_icon="📈",
    layout="wide",
)
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

@st.cache(allow_output_mutation=True)
def train_and_cache_model(predictor):
    with st.spinner("Training the model..."):
        # Call the train_model() method from your class
        predictor.train_model()
        
        predictions_df = predictor.make_predictions()
        st.dataframe(predictions_df)
        # Save the trained model to a file
        predictor.save_model()  # Add this line to save the model
        st.success("Model has been trained successfully and saved!")

        
        

        
        return predictor  # Return the trained predictor object

def main():
    st.title("Stock Prediction Model")

    # Create a sidebar for user inputs
    st.sidebar.header("User Input")

    # Select a sector
    selected_sector = st.sidebar.selectbox("Select a Sector", ["Energy", "Financial", "Technology"])

    # Initialize predictor as None and data_is_ready as False
    predictor = None
    data_is_ready = False

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

        # Check if a valid company is selected
        if selected_company:
            ticker_symbol = selected_dict[selected_company]
            st.sidebar.write(f"Ticker Symbol for {selected_company}: {ticker_symbol}")

            # Initialize predictor with the selected ticker symbol
            predictor = StockModelTrainerPredictor(ticker_symbol)

            # Button to fetch and combine data for model training
            fetch_data_button = st.sidebar.button("Fetch Data for Training")
            if fetch_data_button:
                with st.spinner("Fetching and combining data for training..."):
                    # Use the class method to fetch and combine data
                    combined_data = predictor.get_combined_data()

                # Display the combined data
                st.subheader("Combined Data for Model Training")
                st.write(combined_data)

                # Update the data_is_ready flag
                data_is_ready = True

                # Automatically preprocess data
                with st.spinner("Preprocessing data..."):
                    # Set the ticker attribute for the predictor object
                    predictor.ticker = ticker_symbol

                    # Call the preprocess_data() method from your class
                    predictor.preprocess_data()
                st.success("Data has been preprocessed successfully!")

                # Train and cache the model
                predictor = train_and_cache_model(predictor)

                

            # # Button to download the trained model
            # if data_is_ready:
            #     # ... (Rest of your code for visualization and prediction)
            #     visualize_whole_data_button = st.sidebar.button("Visualize Results - Whole Data")
            #     if visualize_whole_data_button:
            #         # Call the visualize_results_whole() method from your class
            #         predictor.visualize_results_whole()

            #     # Button to visualize results for the next 60 days
            #     visualize_60_days_button = st.sidebar.button("Visualize Results - Next 60 Days")
            #     if visualize_60_days_button:
            #         # Call the visualize_results_60days() method from your class
            #         predictor.visualize_results_60days()

            #     # Button to calculate and display average RMSE
            #     calculate_rmse_button = st.sidebar.button("Calculate Average RMSE")
            #     if calculate_rmse_button:
            #         # Call the calculate_average_rmse() method from your class
            #         predictor.calculate_average_rmse()

            #     # Button to calculate and display average MAPE
            #     calculate_mape_button = st.sidebar.button("Calculate Average MAPE")
            #     if calculate_mape_button:
            #         # Call the calculate_average_mape() method from your class
            #         predictor.calculate_average_mape()

            #     # Button to calculate and display average Pearson correlation coefficient
            #     calculate_corr_button = st.sidebar.button("Calculate Average Pearson Correlation")
            #     if calculate_corr_button:
            #         # Call the calculate_average_pearson_corr() method from your class
            #         predictor.calculate_average_pearson_corr()

            #     # Button to predict and visualize the next 60 days
            #     predict_60_days_button = st.sidebar.button("Predict Next 60 Days")
            #     if predict_60_days_button:
            #         # Call the predict_next_60_days() method from your class
            #         predictor.predict_next_60_days()
            #     # Button to visualize results for the whole data
if __name__ == "__main__":
    main()
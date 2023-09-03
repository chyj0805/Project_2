import streamlit as st
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
# Your Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = "4FHTO2GAT3NL1EZ8"
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

def fetch_stock_data(ticker_symbol):
    ts = TimeSeries(key='4FHTO2GAT3NL1EZ8', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker_symbol,interval='1min', outputsize='full')
    return data

def main():
    st.title("Company Ticker Lookup")

    # Dropdown to select a category
    selected_category = st.selectbox("Select a Category", ["Energy", "Financial", "Technology"])

    # Display the selected category's dropdown and ticker symbol
    if selected_category == "Energy":
        selected_company = st.selectbox("Select an Energy Company", list(energy_data.keys()))
        if selected_company in energy_data:
            ticker_symbol = energy_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker_symbol}")
            # Fetch historical stock data using Alpha Vantage API
            stock_data = fetch_stock_data(ticker_symbol)
            # Display the DataFrame using st.dataframe
            with st.container():
                st.dataframe(stock_data)
        
        else:
            st.write("Please select an energy company.")
    elif selected_category == "Financial":
        selected_company = st.selectbox("Select a Financial Company", list(finn_data.keys()))
        if selected_company in finn_data:
            ticker_symbol = finn_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker_symbol}")
            # Fetch historical stock data using Alpha Vantage API
            stock_data = fetch_stock_data(ticker_symbol)
            # Display the DataFrame using st.dataframe
            with st.container():
                st.dataframe(stock_data)
        else:
            st.write("Please select a financial company.")
    elif selected_category == "Technology":
        selected_company = st.selectbox("Select a Technology Company", list(tech_data.keys()))
        if selected_company in tech_data:
            ticker_symbol = tech_data[selected_company]
            st.write(f"Ticker Symbol for {selected_company}: {ticker_symbol}")
            st.header((f"{selected_company}Historical Stock Data:"))
            # Fetch historical stock data using Alpha Vantage API
            stock_data = fetch_stock_data(ticker_symbol)
            # Display the DataFrame using st.dataframe
            with st.container():
                st.dataframe(stock_data)
        else:
            st.write("Please select a technology company.")

        
        
        


if __name__ == "__main__":
    main()
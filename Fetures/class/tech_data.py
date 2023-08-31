import pandas as pd
import alpha_vantage

class AlphaVantageClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.av_client = alpha_vantage.AlphaVantage(key=api_key, output_format='pandas')
        
    def fetch_stock_data(self, symbol, interval='daily'):
        data, _ = self.av_client.get_timeseries(symbol=symbol, interval=interval, outputsize='full')
        return data

def create_dataframe_from_features(api_key, symbol, features, interval='daily'):
    av_client = AlphaVantageClient(api_key)
    stock_data, _ = av_client.fetch_stock_data(symbol, interval=interval)
    
    selected_features = ['date', *features]
    selected_data = stock_data[selected_features]
    
    return selected_data

# Example usage
api_key = "your_alpha_vantage_api_key"
symbol = "AAPL"
selected_features = ['open', 'high', 'low', 'close', 'volume']
interval = 'daily'

dataframe = create_dataframe_from_features(api_key, symbol, selected_features, interval)
print(dataframe)


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
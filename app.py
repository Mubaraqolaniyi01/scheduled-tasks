import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# 1. Page Configuration
st.set_page_config(page_title="Infra Macro Dashboard", layout="wide")
st.title("🌐 Global Infrastructure Macro-Sensitivity Dashboard")
st.markdown("Developed by **Mubaraq Olaniyi** | UCL Infrastructure Investment & Finance")

# 2. Data Setup
info_map = {
    'EQIX': 'Equinix (Digital)',
    'NEE': 'NextEra (Energy)',
    'BIP': 'Brookfield (Diversified)',
    'DG.PA': 'Vinci (Transport)',
    'ADANIPORTS.NS': 'Adani Ports (EM Wildcard)'
}
tickers = list(info_map.keys())

# 3. Sidebar for User Control
st.sidebar.header("Settings")
years = st.sidebar.slider("Select Year Range", 1, 10, 5)

# 4. Fetch Data
@st.cache_data # This makes the website fast by "remembering" data
def load_data(yrs):
    all_data = yf.download(tickers + ['^TNX'], period=f"{yrs}y")['Close']
    return all_data

data = load_data(years)
stocks = data[tickers]
rates = data['^TNX']

# 5. Calculate Correlation Scores
st.subheader("📊 Macro Sensitivity (Correlation to US 10Y Yield)")
cols = st.columns(len(tickers))

for i, ticker in enumerate(tickers):
    # Calculate the correlation number
    correlation = stocks[ticker].corr(rates)
    
    # Display as a professional "Metric"
    with cols[i]:
        color = "normal" if correlation > 0 else "inverse"
        st.metric(label=info_map[ticker], 
                  value=f"{correlation:.2f}", 
                  delta="Inverse Correlation" if correlation < 0 else "Positive Correlation",
                  delta_color=color)

# 6. Visual Chart
st.subheader("📈 Visual Comparison: Stock Price vs. Interest Rates")
selected_stock = st.selectbox("Select a company to visualize details:", tickers, format_func=lambda x: info_map[x])

fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(stocks[selected_stock], color='navy', label='Stock Price')
ax1.set_ylabel("Price (Local Currency)", color='navy')

ax2 = ax1.twinx()
ax2.plot(rates, color='red', linestyle='--', alpha=0.5, label='US 10Y Yield')
ax2.set_ylabel("US 10Y Yield (%)", color='red')

plt.title(f"{info_map[selected_stock]} Sensitivity Analysis", fontweight='bold')
st.pyplot(fig)
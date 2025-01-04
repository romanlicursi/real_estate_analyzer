import os
import sys
import streamlit as st
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.data.api_client import fetch_property_data, analyze_properties_with_financials
from src.visualization.visualizations import plot_roi_bar_chart, plot_price_vs_cash_flow

# Streamlit App
st.title("Real Estate Analysis Tool")
st.sidebar.header("User Inputs")

# User Inputs
location = st.sidebar.text_input(
    "Enter Location", 
    "Madison, WI", 
    help="Enter a city or region to analyze properties."
)
rent = st.sidebar.number_input("Estimated Monthly Rent ($)", min_value=0, value=2500, step=100)
expenses = st.sidebar.number_input("Estimated Monthly Expenses ($)", min_value=0, value=500, step=50)

# Fetch and Analyze Data
if st.sidebar.button("Analyze Properties"):
    st.write(f"Fetching data for {location}...")
    raw_data = fetch_property_data(location)
    if raw_data:
        financial_data = analyze_properties_with_financials(raw_data, rent=rent, expenses=expenses)
        if not financial_data.empty:
            st.write("### Financial Analysis Results", financial_data)
            
            # Visualizations
            st.write("### ROI Bar Chart")
            roi_fig = plot_roi_bar_chart(financial_data)
            st.plotly_chart(roi_fig)

            st.write("### Price vs. Cash Flow Scatter Plot")
            cashflow_fig = plot_price_vs_cash_flow(financial_data)
            st.plotly_chart(cashflow_fig)
        else:
            st.error("No valid properties found.")
    else:
        st.error("Failed to fetch data.")



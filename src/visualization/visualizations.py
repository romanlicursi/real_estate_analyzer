import pandas as pd
import plotly.express as px

def plot_roi_bar_chart(df):
    """
    Creates a bar chart ranking properties by ROI.
    :param df: DataFrame containing property data.
    :return: A Plotly figure object.
    """
    if "roi" in df.columns and "address" in df.columns:
        fig = px.bar(
            df.sort_values(by="roi", ascending=False),
            x="address",
            y="roi",
            title="Properties Ranked by ROI",
            labels={"roi": "Return on Investment (%)", "address": "Property Address"},
        )
        return fig
    else:
        raise ValueError("Required columns ('roi', 'address') are missing in DataFrame.")

def plot_price_vs_cash_flow(df):
    """
    Creates a scatter plot showing property price vs. monthly cash flow.
    :param df: DataFrame containing property data.
    :return: A Plotly figure object.
    """
    if "price" in df.columns and "monthly_cash_flow" in df.columns:
        fig = px.scatter(
            df,
            x="price",
            y="monthly_cash_flow",
            title="Price vs. Monthly Cash Flow",
            labels={"price": "Property Price ($)", "monthly_cash_flow": "Monthly Cash Flow ($)"},
        )
        return fig
    else:
        raise ValueError("Required columns ('price', 'monthly_cash_flow') are missing in DataFrame.")


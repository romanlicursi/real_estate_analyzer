import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
import requests
import pandas as pd
from dotenv import load_dotenv
from src.analysis.financial_calculator import FinancialCalculator

# Load the API key from the .env file
load_dotenv(dotenv_path="config/.env")
ZILLOW_API_KEY = os.getenv("ZILLOW_API_KEY")

BASE_URL = "https://zillow-com1.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": ZILLOW_API_KEY,
    "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

def fetch_property_data(location):
    """Fetch property data for a given location."""
    endpoint = f"{BASE_URL}/propertyExtendedSearch"
    params = {"location": location, "status_type": "ForRent"}
    response = requests.get(endpoint, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def clean_property_data(raw_data):
    """Clean and format the raw property data into a DataFrame."""
    properties = raw_data.get("props", [])
    if not properties:
        print("No properties found.")
        return None

    # Convert to DataFrame
    df = pd.DataFrame(properties)

    # Print available columns for debugging
    print("Available columns:", df.columns.tolist())

    # Define columns to keep
    columns_to_keep = ["address", "price", "beds", "baths", "area", "statusText"]
    existing_columns = [col for col in columns_to_keep if col in df.columns]
    print("Columns to keep:", existing_columns)
    df = df[existing_columns]

    # Ensure 'price' is treated as a string before cleaning
    if "price" in df.columns:
        df["price"] = df["price"].astype(str)
        df["price"] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)

    return df

def analyze_properties_with_financials(raw_data, rent=2500, expenses=500):
    """Analyze properties with financial metrics."""
    properties = raw_data.get("props", [])
    results = []

    for prop in properties:
        price = prop.get("price", None)

        # Clean or validate the price
        if isinstance(price, str):  # If price is a string, clean it
            price = price.replace("$", "").replace(",", "")
            if price.isdigit():  # Convert cleaned string to integer
                price = int(price)
            else:
                price = None  # Invalid price

        # Ensure price is an integer
        if isinstance(price, int):
            calculator = FinancialCalculator(price, 20, 5, 30)
            analysis = calculator.analyze_property(rent, expenses)
            analysis["address"] = prop.get("address", "N/A")
            results.append(analysis)

    return pd.DataFrame(results)


def save_data_to_csv(df, filename="property_data.csv"):
    """Save the DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    # Fetch data for a specific location
    raw_data = fetch_property_data("Madison, WI")

    # Debugging: Print raw data structure
    if raw_data:
        print("Raw Data Response:")
        print(raw_data)

    # Clean the data
    if raw_data:
        financial_data = analyze_properties_with_financials(raw_data)
        if not financial_data.empty:
            print("Financial Analysis Results:")
            print(financial_data)
            financial_data.to_csv("financial_analysis.csv", index=False)


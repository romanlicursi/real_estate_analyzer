# Real Estate Analyzer

A Python-based tool for analyzing real estate investments, designed to help identify house-hacking 
opportunities by pulling and processing data from the Zillow API.

## Features
- **API Integration**: Fetch property data using the Zillow API.
- **Data Cleaning**: Process and clean raw property data into a structured format.
- **CSV Export**: Save cleaned property data to a CSV file for further analysis.
- **Expandable Design**: Modular structure for adding financial analysis and visualizations.

## Technology Stack
- **Python**: Core programming language.
- **Pandas**: Data cleaning and processing.
- **Requests**: API interaction.
- **Dotenv**: Securely manage API keys.
- **Zillow API**: Source for real estate data.

## Project Structure
real_estate_analyzer/ │ ├── config/ │ └── .env # Stores API key ├── src/ │ ├── data/ │ 
│ └── api_client.py # Fetch and process property data │ ├── analysis/ # Future financial 
analysis features │ └── visualization/ # Future visualization features ├── tests/ # Unit tests 
├── property_data.csv # Example output CSV └── README.md # Project documentation


## Setup Instructions
**Clone the Repository**:
git clone git@github.com:romanlicursi/real_estate_analyzer.git cd real_estate_analyzer


**Set Up a Virtual Environment**:
python3 -m venv venv source venv/bin/activate # On macOS/Linux


**Install Dependencies**:
pip install -r requirements.txt


**Configure API Access**:
- Create a `.env` file in the `config/` directory:
  ```
  ZILLOW_API_KEY=your_actual_api_key
  ```

**Run the Project**:
python src/data/api_client.py


## Future Features
- **Financial Calculations**:
- Mortgage payment estimation
- ROI and cash flow analysis
- **Interactive Dashboard**:
- Visualize property data with Plotly or Streamlit
- **User Input**:
- Custom filters for location, price range, and property type

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

## License
This project is licensed under the MIT License.

## Contact
Created by **Roman Licursi**. Feel free to connect on [GitHub](https://github.com/romanlicursi).

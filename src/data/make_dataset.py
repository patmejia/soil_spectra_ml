import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

# Data Preprocessing

def load_data(filepath, chunk_size=None):
    """
    Load large-scale data using pandas with optional chunking.
    """
    if chunk_size:
        return pd.read_csv(filepath, chunksize=chunk_size)
    else:
        return pd.read_csv(filepath)

def inspect_data(df):
    """
    Provide a summary of the data including missing values and data types.
    """
    print(df.info())
    print(df.head())

def clean_data(df):
    """
    Handle missing values and outliers in spectral columns.
    """
    # Remove rows with missing values
    df.dropna(inplace=True)
    
    # Handle outliers (you can replace this with your specific logic)
    for column in df.select_dtypes(include=[np.number]).columns:
        df = df[np.abs(df[column] - df[column].mean()) <= (3 * df[column].std())]
    
    return df

def transform_data(df):
    """
    Apply transformation A = log10(1/R) if needed.
    """
    # Replace this with actual columns that need transformation
    spectral_columns = [] 
    
    for col in spectral_columns:
        df[col] = np.log10(1 / df[col])
    
    return df

# Main function to execute all the steps
def main():
    # Replace 'your_data.csv' with the actual filepath
    filepath = 'data/raw/ss4gg-hackathon-mir-soil-spectroscopy/train.csv'
    
    # Step 1: Load Data
    df = load_data(filepath)
    
    # Step 2: Inspect Data
    inspect_data(df)
    
    # Step 3: Clean Data
    df_clean = clean_data(df)
    
    # Step 4: Transform Data
    df_transformed = transform_data(df_clean)
    
    # Save the transformed data to interim folder
    df_transformed.to_csv('data/interim/transformed_data.csv', index=False)

if __name__ == '__main__':
    main()

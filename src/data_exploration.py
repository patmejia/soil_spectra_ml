import argparse
import pandas as pd
from pathlib import Path
import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize logging
logging.basicConfig(level=logging.INFO)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data Exploration for Soil Spectroscopy Competition.')
    parser.add_argument('--directory', required=True, help='Path to the directory containing data files.')
    return parser.parse_args()

def read_data_in_batches(file_path, batch_size=1000):
    reader = pd.read_csv(file_path, iterator=True, chunksize=batch_size)
    return reader

def perform_preliminary_exploration(chunk, summary_df):
    logging.info(f"Exploring chunk with {chunk.shape[0]} rows and {chunk.shape[1]} columns.")
    new_summary = chunk.describe().transpose()
    if summary_df is None:
        return new_summary
    else:
        return summary_df.add(new_summary, fill_value=0)

def generate_visual_report(summary_df, directory):
    plt.figure(figsize=(10, 6))
    sns.heatmap(summary_df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.savefig(directory / "reports" / "missing_values_heatmap.png")

def generate_report(summary_df, directory):
    report_path = directory / "reports" / "enhanced_preliminary_report.csv"
    summary_df.to_csv(report_path)
    generate_visual_report(summary_df, directory)
    logging.info(f"Report saved to {report_path}")

def main():
    args = parse_arguments()
    data_dir = Path(args.directory)
    
    summary_df = None
    
    # Create reports directory if it doesn't exist
    reports_dir = data_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # File paths for train and test data
    train_file_path = data_dir / "data/raw/ss4gg-hackathon-mir-soil-spectroscopy/train.csv"
    test_file_path = data_dir / "data/raw/ss4gg-hackathon-mir-soil-spectroscopy/test.csv"
    
    # Read and explore train data
    train_data_reader = read_data_in_batches(train_file_path)
    for chunk in train_data_reader:
        summary_df = perform_preliminary_exploration(chunk, summary_df)
        
    # Generate and save report
    generate_report(summary_df, data_dir)

if __name__ == '__main__':
    main()

import argparse
import pandas as pd
from pathlib import Path
import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data Exploration for Soil Spectroscopy Competition.')
    parser.add_argument('--directory', required=True, help='Path to the directory containing data files.')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging.')
    return parser.parse_args()

def read_data_in_batches(file_path, batch_size=1000):
    return pd.read_csv(file_path, iterator=True, chunksize=batch_size)

def summarize_missing_values(data_reader):
    missing_values_summary = pd.Series(dtype=int)
    total_chunks = 0
    for chunk in data_reader:
        total_chunks += 1
        missing_values_summary = missing_values_summary.add(chunk.isnull().sum(), fill_value=0)
    return missing_values_summary, total_chunks

def generate_visual_report(summary_df, directory):
    plt.figure(figsize=(10, 6))
    sns.heatmap(summary_df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.savefig(directory / "reports" / "missing_values_heatmap.png")

def main():
    args = parse_arguments()
    data_dir = Path(args.directory)
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    logging.info("Starting data exploration process.")
    train_file_path = data_dir / "data/raw/ss4gg-hackathon-mir-soil-spectroscopy/train.csv"
    
    # Read and summarize train data
    train_data_reader = read_data_in_batches(train_file_path)
    missing_values_summary, total_chunks = summarize_missing_values(train_data_reader)
    
    if missing_values_summary.sum() == 0:
        logging.info("No missing values found in the dataset.")
    else:
        logging.info(f"Missing values summary across {total_chunks} chunks:\n{missing_values_summary}")

    # Create reports directory if it doesn't exist
    reports_dir = data_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate and save report
    report_path = reports_dir / "preliminary_report.csv"
    missing_values_summary.to_csv(report_path)
    logging.info(f"Missing values report saved to {report_path}")
    
    # Generate visual report if there are missing values
    if missing_values_summary.sum() > 0:
        generate_visual_report(missing_values_summary.to_frame().transpose(), data_dir)
        logging.info(f"Missing values heatmap saved to {reports_dir / 'missing_values_heatmap.png'}")
    
    logging.info("Data exploration process completed.")

if __name__ == '__main__':
    main()

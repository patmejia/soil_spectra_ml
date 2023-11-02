import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.decomposition import PCA
import numpy as np

def parse_arguments():
    parser = argparse.ArgumentParser(description='In-depth Data Analysis for Soil Spectroscopy.')
    parser.add_argument('--data_dir', required=True, help='Directory containing the dataset.')
    return parser.parse_args()

def process_chunk(chunk, target_columns):
    summary = chunk[target_columns].describe()
    return summary

def analyze_correlations(df, output_dir):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    high_corr_pairs = corr_matrix.abs()[(corr_matrix > 0.8) & (corr_matrix < 1.0)].stack().reset_index()
    high_corr_pairs.columns = ['Variable 1', 'Variable 2', 'Correlation']
    high_corr_pairs.to_csv(output_dir / 'high_correlation_pairs.csv', index=False)
    return high_corr_pairs

def plot_distribution(df, column, output_dir):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True, bins=25)
    plt.xlabel(f'{column} Percentage')
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.savefig(output_dir / f'{column}_distribution.png')
    plt.close()

def perform_pca(df, output_dir):
    # Ensure spectral columns are selected correctly and are numeric
    spectral_columns = df.columns[df.columns.str.contains('spectral') & df.dtypes.isin([np.dtype('float64'), np.dtype('int64')])]
    if spectral_columns.empty:
        print("No spectral columns found or spectral columns are not numeric.")
        return

    pca = PCA()
    pca.fit(df[spectral_columns])
    explained_variance = pca.explained_variance_ratio_
    plt.figure(figsize=(8, 6))
    plt.plot(np.cumsum(explained_variance))
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('PCA Explained Variance')
    plt.tight_layout()
    plt.savefig(output_dir / 'pca_explained_variance.png')
    plt.close()

def main():
    args = parse_arguments()
    data_dir = Path(args.data_dir)
    output_dir = data_dir / 'outputs'
    output_dir.mkdir(parents=True, exist_ok=True)

    target_columns = ['clay_perc', 'sand_perc', 'silt_perc']
    summary_frames = []

    for chunk in pd.read_csv(data_dir / 'train.csv', chunksize=10000):
        summary_frames.append(process_chunk(chunk, target_columns))
    
    # Combine all summaries
    target_summary = pd.concat(summary_frames).groupby(level=0).mean()
    target_summary.to_csv(output_dir / 'target_summary.csv')
    print(target_summary)

    # Assuming the dataset fits into memory for correlation analysis
    train_df = pd.concat(summary_frames)
    print(analyze_correlations(train_df, output_dir))

    for target in target_columns:
        plot_distribution(train_df, target, output_dir)

    perform_pca(train_df, output_dir)

if __name__ == '__main__':
    main()

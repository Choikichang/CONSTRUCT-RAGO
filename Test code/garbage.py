import pandas as pd

def tsv_to_csv(tsv_file_path, csv_file_path):
    """
    Convert a TSV file to a CSV file.

    Parameters:
        tsv_file_path (str): Path to the input TSV file.
        csv_file_path (str): Path to save the output CSV file.
    """
    try:
        # Read the TSV file
        data = pd.read_csv(tsv_file_path, sep='\t')

        # Save as CSV file
        data.to_csv(csv_file_path, index=False)

        print(f"Conversion completed. CSV file saved at: {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'input.tsv' and 'output.csv' with your file paths
ts_file = "/media/choi/HDD1/mmaction2/data/Korea_construction_standard/Con_NLI_cleaned.tsv"
csv_file = "/media/choi/HDD1/mmaction2/data/Korea_construction_standard/Con_NLI_cleaned_2.csv"
tsv_to_csv(ts_file, csv_file)
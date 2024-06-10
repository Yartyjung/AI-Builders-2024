import os
import csv

def merge_csv_files(folder_path, output_file_path):
    """
    Function to merge all CSV files in a given folder into a single CSV file.
    """
    # List to store the header and rows
    merged_data = []
    header_saved = False

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', newline='',encoding="utf8") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if not header_saved:
                    merged_data.append(header)
                    header_saved = True
                for row in reader:
                    merged_data.append(row)

    # Write merged data to the output file
    with open(output_file_path, 'w', newline='',encoding="utf8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(merged_data)

if __name__ == "__main__":
    # Specify the folder path containing the CSV files
    folder_path = R'C:\Users\User\Documents\GitHub\AI-Builders-2024\data copy'
    # Specify the output file path
    output_file_path = 'review summarizer/merged2.csv'
    
    # Merge the CSV files
    merge_csv_files(folder_path, output_file_path)

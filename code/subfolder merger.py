import os
import csv

def merge_csv_files(folder_path, output_file_path):
    merged_data = []
    header_saved = False

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                file_path = os.path.join(root, filename)
                print(f"Processing file: {file_path}")
                try:
                    # Read CSV file
                    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                        reader = csv.reader(csvfile)
                        header = next(reader)
                        if not header_saved:
                            merged_data.append(header)
                            header_saved = True
                        for row in reader:
                            merged_data.append(row)
                except Exception as e:
                    print(f"Error reading file: {file_path}")
                    print(e)

    # Write merged data
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(merged_data)

if __name__ == "__main__": 
    folder_path = 'data copy'
    output_file_path = 'review summarizer/merged2.csv'
    merge_csv_files(folder_path, output_file_path)

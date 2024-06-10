import os

def transform_line(line):
    """
    Function to transform a line of the text.
    Modify this function to apply the desired transformation.
    """
    # Prepend and append text to each line
    return line.strip() + '|real\n'

def process_text_file(file_path):
    """
    Function to read, edit, and save a text file.
    """
    with open(file_path, 'r',encoding="utf8") as file:
        lines = file.readlines()

    with open(file_path, 'w',encoding="utf8") as file:
        for line in lines:
            file.write(transform_line(line))

def process_folder(folder_path):
    """
    Function to process all text files in a given folder.
    """
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                file_path = os.path.join(root, filename)
                process_text_file(file_path)

if __name__ == "__main__":
    # Specify the folder path containing the CSV files
    folder_path = 'data copy'
    
    # Process the folder
    process_folder(folder_path)

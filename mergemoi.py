import pandas as pd

def convert_to_nothing(filename):
    # Path of the uploaded file
    input_file_path = f'{filename}.xlsx'
    output_file_path = f'{filename}_UTF8.csv'

    # Load the Excel file
    data = pd.read_excel(input_file_path)

    # Save as CSV with UTF-8 encoding
    data.to_csv(output_file_path, index=False, encoding='utf-8', sep=';')

    return output_file_path

convert_to_nothing('StringTable')
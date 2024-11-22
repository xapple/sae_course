import pandas as pd

def convertIntoCSVFromXlsx(StringValue):
    # Path of the uploaded file
    input_file_path = f'{StringValue}.xlsx'
    output_file_path = f'{StringValue}_UTF8.csv'

    # Load the Excel file
    data = pd.read_excel(input_file_path)

    # Save as CSV with UTF-8 encoding
    data.to_csv(output_file_path, index=False, encoding='utf-8', sep=';')

    return output_file_path

convert_to_CSV('StringTable')
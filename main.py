"""
This script serves as the main entry point for converting PDF and PNG files
containing tables into CSV format.

The script prompts the user to enter a file path and processes the file based
on its extension. If a PDF file is provided, it is first converted into a
series of PNG images, one for each page. Each PNG image is then processed to
extract tabular data, which is subsequently written to a CSV file. If a PNG
file is provided, it is processed directly.

The script relies on three modules:
- `PDF2PNG`: To convert PDF files to PNG images.
- `recognition`: To extract tabular data from PNG images.
- `writeToCSV`: To write the extracted data to a CSV file.
"""
from PDF2PNG import convert_pdf2png
from recognition import parse_img_to_csv_data
from writeToCSV import write_csv


if __name__ == "__main__":
    """
    Main execution block of the script.

    Prompts the user to enter a file path and processes the file based on its
    extension. If the file is a PDF, it is converted to PNG images, and each
    image is processed to extract tabular data, which is then written to a CSV
    file. If the file is a PNG, it is processed directly. If the file format
    is not supported, an error message is displayed.
    """
    input_file = str(input("Введите путь файла: "))
    if ".pdf" in input_file:
        new_input_file = input_file.replace("\\", "\\\\")
        files = convert_pdf2png(new_input_file)
        for file in files:
            data = parse_img_to_csv_data(file)
            # print(data)
            write_csv(file.replace(".png", ".csv"), data)

    elif ".png" in input_file:
        new_input_file = input_file.replace("\\", "\\\\")
        data = parse_img_to_csv_data(new_input_file)
        # print(data)
        write_csv(new_input_file.replace(".png", ".csv"), data)
    else:
        print("Файл с данным форматом не поддерживается. Используйте PNG или PDF.")

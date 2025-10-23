"""
This module provides a function for writing data to a CSV file.

It takes a file path and a list of lists, and writes the data to the specified
CSV file.
"""
import csv
import os


def write_csv(path, data):
    """Writes a list of lists to a CSV file.

    This function takes a file path and a list of lists, and writes the data
    to a CSV file. Each inner list is written as a row in the CSV file.

    Args:
        path: The file path for the output CSV file.
        data: A list of lists representing the data to be written.
    """
    file_path = str(os.getcwd())+"\\"+str(path)

    with open(file_path, "w", newline='', encoding='cp1251') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for index, item in enumerate(data):
            writer.writerows([item])
    print(f"Запись файла: {os.path.basename(file_path)} - завершена!\n")
    print("#"*66)

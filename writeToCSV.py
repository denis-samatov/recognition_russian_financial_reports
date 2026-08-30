"""
This module provides a function for writing data to a CSV file.

It takes a file path and a list of lists, and writes the data to the specified
CSV file.
"""
import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def write_csv(path: Path, data) -> None:
    """Writes a list of lists to a CSV file.

    This function takes a file path and a list of lists, and writes the data
    to a CSV file. Each inner list is written as a row in the CSV file.

    Args:
        path: The file path for the output CSV file.
        data: A list of lists representing the data to be written.
    """
    file_path = path if path.is_absolute() else Path.cwd() / path

    # cp1251 matches the encoding Russian-locale Excel expects when opening
    # this CSV directly, rather than utf-8.
    with open(file_path, "w", newline='', encoding='cp1251') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for item in data:
            writer.writerows([item])
    logger.info("File written: %s - done!\n", file_path.name)
    logger.info("#" * 66)

# PDF to CSV Converter

This Python script is designed to convert PDF and PNG files containing tables into CSV format. The script uses computer vision and optical character recognition (OCR) to extract tabular data from images and saves it in a structured CSV file.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)

## Getting Started

Follow these instructions to set up and run the script on your local machine.

### Prerequisites

- Python 3.x
- Tesseract OCR Engine

You can download and install Tesseract from the [official repository](https://github.com/tesseract-ocr/tesseract).

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports.git
    ```
2.  Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file for this to work. See the [Dependencies](#dependencies) section for a list of required libraries.)*

### Usage

1.  Run the `main.py` script from the command line:
    ```sh
    python main.py
    ```
2.  When prompted, enter the full path to the PDF or PNG file you want to process.
3.  The script will generate a CSV file with the extracted data in the same directory.

## How It Works

The script processes the input file in the following steps:

1.  **File Handling:**
    - If the input file is a PDF, it is converted into a series of PNG images, one for each page.
    - If the input file is a PNG, it is processed directly.

2.  **Image Processing:**
    - The image is converted to grayscale and then to a binary format to improve the accuracy of text recognition.
    - The script identifies the horizontal and vertical lines of the table to determine the cell coordinates.

    <div align="center">
        <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_1.png" alt="Table Image">
    </div>

3.  **Data Extraction:**
    - The content of each cell is extracted using the calculated coordinates.
    - The text from each cell is recognized using the Tesseract OCR engine.

    <div align="center">
        <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_2.png" alt="Horizontal Table Lines">
        <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_3.png" alt="Vertical Table Lines">
    </div>

4.  **CSV Generation:**
    - The extracted data is written to a CSV file.

## Dependencies

This script relies on the following Python libraries:

-   **PyMuPDF (`fitz`)**: For converting PDF files to PNG images.
-   **OpenCV-Python (`cv2`)**: For image processing and table detection.
-   **NumPy**: For numerical operations and handling image data.
-   **Pytesseract**: For optical character recognition (OCR).
-   **Matplotlib**: For data visualization.

You can install these libraries using pip:

```sh
pip install PyMuPDF opencv-python numpy pytesseract matplotlib
```

## Disclaimer

This script is provided "as is." The results may vary depending on the nature and complexity of the tables in the input files. It is recommended to carefully review the generated CSV files for accuracy before using them.

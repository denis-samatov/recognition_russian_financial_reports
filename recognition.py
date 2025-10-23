"""
This module provides functions for recognizing and extracting tabular data from
images.

It uses computer vision techniques to identify the cell coordinates of a table
in an image, extracts the text from each cell using optical character
recognition (OCR), and returns the data in a structured format.
"""

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pytesseract
import re


def parse_img_to_csv_data(src):
    """Extracts tabular data from an image.

    This function processes an image to identify a table structure, extracts
    the text from each cell using OCR, and returns the data as a list of lists.

    The process involves the following steps:
    1.  Convert the image to grayscale and then to a binary format.
    2.  Detect horizontal and vertical lines to identify the table structure.
    3.  Find the intersection points of the lines to determine the cell
        coordinates.
    4.  Extract the content of each cell and convert it to text using OCR.
    5.  Clean the extracted text by removing special characters.

    Args:
        src: The file path of the input image.

    Returns:
        A list of lists representing the tabular data, where each inner list
        corresponds to a row in the table.
    """
    raw = cv.imread(src, 1)

    # Изображение в оттенках серого
    gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)

    # Бинаризация
    binary = cv.adaptiveThreshold(~gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, -5) # выбрать пятый параметр 21
    # plt.imshow(binary,'gray')
    # plt.show()
    rows, cols = binary.shape

    # Определение горизонтальных линий
    scale = 40 # можно поставить значение от 20-60
    mask = cv.getStructuringElement(cv.MORPH_RECT, (cols // scale, 1))
    eroded = cv.erode(binary, mask, iterations=1)
    dilated_col = cv.dilate(eroded, mask, iterations=1)
    # plt.imshow(dilated_col,'gray')
    # plt.show()

    # Определение вертикальных линий
    scale = 20 # можно поставить значение от 10-30
    mask = cv.getStructuringElement(cv.MORPH_RECT, (1, rows // scale))
    eroded = cv.erode(binary, mask, iterations=1)
    dilated_row = cv.dilate(eroded, mask, iterations=1)
    # plt.imshow(dilated_row,'gray')
    # plt.show()

    # Определение пересечений
    bitwise_and = cv.bitwise_and(dilated_col, dilated_row) # побитовое И истинно тогда и только тогда, когда оба пикселя больше нуля
    # plt.imshow(bitwise_and,'gray')
    # plt.show()

    # # Идентификационная форма таблицы
    # merge = cv.add(dilated_col, dilated_row) # по факту ненужная вещь
    # # plt.imshow(merge,'gray')
    # # plt.show()

    # # Удаление рамок таблицы
    # merge2 = cv.subtract(binary, merge) # по факту ненужная вещь
    # # plt.imshow(merge2,'gray')
    # # plt.show()

    # new_kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2)) # по факту ненужная вещь
    # erode_image = cv.morphologyEx(merge2, cv.MORPH_OPEN, new_kernel)
    # # plt.imshow(erode_image,'gray')
    # # plt.show()

    # merge3 = cv.add(erode_image, bitwise_and) # по факту ненужная вещь
    # # plt.imshow(merge3,'gray')
    # # plt.show()

    # Определение белых пересечений на черно-белом изображении и выведение горизонтальных и вертикальных координат
    y_point, x_point = np.where(bitwise_and > 0)
    # Ордината
    y_point_arr = []
    # Абсцисса
    x_point_arr = []

    # Путем сортировки получаем значения x и y перехода, указывающие, что это точка пересечения, в противном случае в точке пересечения будет много значений пикселей с аналогичными значениями. Я беру только последнюю точку аналогичного значения.
    # Переход этого 10 не фиксирован. Он будет точно настроен в соответствии с различными изображениями. В основном это высота (переход по координате y) и длина (переход по координате x) таблицы ячеек.
    i = 0
    sort_x_point = np.sort(x_point)
    for i in range(len(sort_x_point) - 1):
        if sort_x_point[i + 1] - sort_x_point[i] > 10:
            x_point_arr.append(sort_x_point[i])
        i = i + 1
    x_point_arr.append(sort_x_point[i])  # Чтобы добавить последнюю точку

    i = 0
    sort_y_point = np.sort(y_point)
    for i in range(len(sort_y_point) - 1):
        if (sort_y_point[i + 1] - sort_y_point[i] > 10):
            y_point_arr.append(sort_y_point[i])
        i = i + 1
    y_point_arr.append(sort_y_point[i]) # Чтобы добавить последнюю точку

    # print("Список координат x", x_point_arr)
    # print("Список координат y", y_point_arr)

    # Циклическая таблица разделения координат y и координат x
    data = [[] for i in range(len(y_point_arr))]
    for i in range(len(y_point_arr) - 1):
        for j in range(len(x_point_arr) - 1):

            # При делении первым параметром является координата y, а вторым параметром - координата x
            cell = raw[y_point_arr[i]:y_point_arr[i + 1], x_point_arr[j]:x_point_arr[j + 1]]
            # plt.imshow(cell)
            # plt.show()

            # Считывает информацию с ячейки
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            text = pytesseract.image_to_string(cell, lang="rus")

            # Удалить специальные символы
            text = re.findall(r'[^\*"$@&/?\\|<>~`″′‖{}!#〈\n]', text, re.S)
            text = "".join(text)
            # print("Информация о изображении ячейки：" + text)
            data[i].append(text)
            j = j + 1
        i = i + 1

    return data

# # # Python3 program to convert image to pdf
# # # using img2pdf library
# # import PyPDF2
# # # importing necessary libraries
# # import img2pdf
# # from PIL import Image
# # import os
# #
# # # storing image path
# # img_path = r"C:\Users\Vrdella\Downloads\pexels-alexas-fotos-2255441.jpg"
# #
# # converted_filename='converted_file.pdf'
# # pdf_path = os.path.join(os.getcwd(),converted_filename)
# #
# # image = Image.open(img_path)
# #
# # # converting into chunks using img2pdf
# # pdf_bytes = img2pdf.convert(image.filename)
# #
# # # opening or creating pdf file
# # file = open(pdf_path, "wb")
# #
# # # writing pdf files with chunks
# # file.write(pdf_bytes)
# #
# # # closing image file
# # image.close()
# #
# # # closing pdf file
# # file.close()
# #
# # # output
# # print("Successfully made pdf file")
# # text_output_path = os.path.join(os.getcwd(), 'extracted_text.txt')
# # with open(pdf_path, 'rb') as pdf_file:
# #     reader = PyPDF2.PdfReader(pdf_file)
# #
# #     # Create a text file to store the extracted text
# #     with open(text_output_path, 'w', encoding='utf-8') as text_file:
# #         # Iterate through all pages
# #         for page_number in range(len(reader.pages)):
# #             # Extract text from the page
# #             page = reader.pages[page_number]
# #             text = page.extract_text()
# #
# #             # Write the text to the text file
# #             text_file.write(text)
# #
# # # Output
# # print("Successfully made pdf file")
# # print(f"Text extracted and saved to {text_output_path}")
#
# import img2pdf
# from PIL import Image
# import os
# import pytesseract
# from pdf2image import convert_from_path
#
# # storing image path
# img_path = r"C:\Users\Vrdella\Downloads\letter-of-application-40.jpg"
#
# converted_filename = 'converted_file.pdf'
# pdf_path = os.path.join(os.getcwd(), converted_filename)
#
# image = Image.open(img_path)
#
# # converting into chunks using img2pdf
# pdf_bytes = img2pdf.convert(image.filename)
#
# # opening or creating pdf file
# file = open(pdf_path, "wb")
#
# # writing pdf files with chunks
# file.write(pdf_bytes)
#
# # closing image file
# image.close()
#
# # closing pdf file
# file.close()
#
# # output
# print("Successfully made pdf file")
#
# # Extract text using Tesseract OCR
# text_output_path = os.path.join(os.getcwd(), 'extracted_text.txt')
#
# from PyPDF2 import PdfReader
#
# # creating a pdf reader object
# reader = PdfReader(converted_filename)
#
# # printing number of pages in pdf file
# # print(len(reader.pages))
#
# # getting a specific page from the pdf file
# page = reader.pages[0]
#
# # extracting text from page
# text = page.extract_text()
# print(text)


import pytesseract
# from pytesseract import Output
# from PIL import Image
# import cv2

img_path1 = r"C:\Users\Vrdella\Downloads\letter-of-application-40.jpg"
text = pytesseract.image_to_string(img_path1,lang='eng')
print(text)
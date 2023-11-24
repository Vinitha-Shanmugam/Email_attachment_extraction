import zlib
import base64

# Read the original text from the text file
with open(r"C:\Users\Vrdella\Documents\skill id.txt", 'r') as file:
    original_text = file.read()

# Compress the text using zlib
compressed_text = zlib.compress(original_text.encode('utf-8'), level=zlib.Z_BEST_COMPRESSION)

# Encode the compressed data in base64
base64_compressed_text = base64.b64encode(compressed_text).decode('utf-8')

# Now you can send 'base64_compressed_text' as a response to the client

# On the receiving end, decode the base64 data
received_base64_compressed_text = base64_compressed_text  # Simulating receiving the data

# Decode the base64 data
compressed_data = base64.b64decode(received_base64_compressed_text)

# Decompress the data using zlib
original_text = zlib.decompress(compressed_data).decode('utf-8')
file1 = open('skilll.txt', 'w')
file1.write(original_text)
file1.close()
# Now 'original_text' contains the original text

#Image to pdf

#
# import pytesseract
# # from pytesseract import Output
# # from PIL import Image
# # import cv2
#
# img_path1 = r"C:\Users\Vrdella\Downloads\letter-of-application-40.jpg"
# text = pytesseract.image_to_string(img_path1,lang='eng')
# print(text)
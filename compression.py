# import zlib
#
#
# def compress_text(input_text):
#     compressed_data = zlib.compress(input_text.encode('utf-8'))
#     return compressed_data
#
#
# def decompress_text(compressed_data):
#     decompressed_text = zlib.decompress(compressed_data).decode('utf-8')
#     return decompressed_text
#
#
# # Example usage:
# original_text = "This is a sample text to be compressed."
# compressed_data = compress_text(original_text)
# decompressed_text = decompress_text(compressed_data)
# print("Original Text:", original_text)
# print("Compressed Text:", compressed_data)
# print("Decompressed Text:", decompressed_text)
import zipfile

# def compress_files(zip_filename, files_to_compress):
#     with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for file in files_to_compress:
#             zipf.write(file)
#
#
# # Example usage:
# files_to_compress = ['file1.txt', 'file2.txt']
# zip_filename = 'compressed_files.zip'
# compress_files(zip_filename, files_to_compress)
import gzip_algo


def compress_text_file(input_file, output_file):
    with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)


# Example usage:
input_file = 'file1.txt'
output_file = 'compressed_output.gz'
compress_text_file(input_file, output_file)

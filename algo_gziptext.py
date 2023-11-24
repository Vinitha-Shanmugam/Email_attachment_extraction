# import gzip
#
# # Input text file
# input_file = 'file1.txt'
#
# # Output compressed file
# output_file = 'compressed.gz'
#
# with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
#     f_out.writelines(f_in)
#
# print("File compressed successfully.")
import lzma

# Input text file
input_file = 'file1.txt'

# Output compressed text file
output_file = 'file123.txt'

with open(input_file, 'rb') as f_in, lzma.open(output_file, 'wb') as f_out:
    f_out.write(f_in.read())

print("File compressed successfully.")

import ctypes
import base64
import subprocess
import os

# Base64 encoded C code for printing "Hello, World!"
encoded_c_code = b'''
I2luY2x1ZGUgPHN0ZGlvLmg+CmludCBtYWluKCkgewogICAgcHJpbnRmKCJIZWxsbywgVW5pdmVyc2UhXG4iKTsKICAgIHJldHVybiAwOwp9
'''

# Decode the base64 encoded C code
decoded_c_code = base64.b64decode(encoded_c_code).decode('utf-8')

# Save the decoded C code to a temporary file
with open('temp.c', 'w') as f:
    f.write(decoded_c_code)

# Compile the C code
subprocess.run(['gcc', 'temp.c', '-o', 'temp_file'])

# Load the compiled C code as a shared library
hello_lib = ctypes.CDLL('./temp_file')

# Call the main function to print "Hello, World!"
hello_lib.main()

# Cleanup: remove the temporary files
os.remove('temp.c')
os.remove('temp_file')

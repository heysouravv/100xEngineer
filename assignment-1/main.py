import ctypes
import base64
import subprocess
import os

# Base64 encoded C code for printing "Hello, World!"
encoded_c_code = b'''
I2luY2x1ZGUgPHN0ZGlvLmg+CmludCBtYWluKCkgewogICAgcHJpbnRmKCJIZWxsbywgV29ybGQhXG4iKTsKICAgIHJldHVybiAwOwp9Cg==
'''

# Decode the base64 encoded C code
decoded_c_code = base64.b64decode(encoded_c_code).decode('utf-8')

# Save the decoded C code to a temporary file
with open('temp_hello.c', 'w') as f:
    f.write(decoded_c_code)

# Compile the C code
subprocess.run(['gcc', 'temp_hello.c', '-o', 'temp_hello'])

# Load the compiled C code as a shared library
hello_lib = ctypes.CDLL('./temp_hello')

# Call the main function to print "Hello, World!"
hello_lib.main()

# Cleanup: remove the temporary files
os.remove('temp_hello.c')
os.remove('temp_hello')

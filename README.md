# Python Obfuscator Script

## Description

This Python script is designed to obfuscate and encrypt Python source code files. It uses a combination of compression and encoding techniques to make the original code difficult to read or reverse engineer. The obfuscation process enhances the security of the code, making it harder for unauthorized users to understand or modify it.

## Features

- **File Input**: Drag and drop your Python file to be obfuscated.
- **Compression**: Utilizes `zlib` and `lzma` to compress the code, reducing file size and adding an additional layer of obfuscation.
- **Encryption**: The script compiles the input code into bytecode and encrypts it using the `marshal` module.
- **Output**: Saves the obfuscated code as a new Python file with the suffix `-obf.py`.

## Usage

1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Install the required dependencies if needed.
4. Run the script using the command:
   ```bash
   python Obfuscator.py

When prompted, drag and drop the Python file you want to obfuscate.
The obfuscated file will be saved in the same directory with the suffix -obf.py.
## Requirements
Python 3.x
``colorama`` library (for colored terminal output)
## License 
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

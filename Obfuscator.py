import os
import zlib
import lzma
from marshal import dumps, loads
from colorama import Fore, init

init()
os.system('cls' if os.name == 'nt' else 'clear')

def red_text(text):
    red = 31
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[{red}m{line}\033[0m\n")
    return faded

print(red_text(''' 
 ██████╗ ██████╗ ███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══██╗██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██████╔╝██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

'''))

file = input(Fore.RED + 'Drag and drop your file here: ' + Fore.RESET)

def compress(text):
    compressed = zlib.compress(text.encode())
    compressed = lzma.compress(compressed)
    return compressed

def encrypt1(text):
    src = compile(text, 'coduter', 'exec')
    ma = dumps(src)
    compressed_code = compress(f'exec(loads({ma}));')
    encrypted_code = f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compressed_code})))"
    return encrypted_code

def encrypt2(text):
    code = text
    s = compile(code, 'coduter', 'exec')
    maa = dumps(s)
    stub2 = f'from marshal import loads;exec(loads({maa}));'
    final_code = f'{stub2}'
    return final_code

if not os.path.isfile(file):
    print(Fore.RED + 'File not found' + Fore.RESET)
    exit()

print(Fore.RED + '\n[+] Encrypting ...' + Fore.RESET)

with open(file, 'r', encoding='utf-8') as f:
    code = f.read()

code = encrypt1(code)
code = encrypt2(code)

print(Fore.RED + '[+] Done' + Fore.RESET)

name = os.path.basename(file).split('.')[0]
with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED + f'Done! Your file is encrypted and saved as {name}-obf.py' + Fore.RESET)
print(Fore.RED + '\n[+] Thank you for using the tool' + Fore.RESET)

import time
time.sleep(2)
os.system('cls')
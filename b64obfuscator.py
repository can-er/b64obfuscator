"""
Author: GorillaGlue
pip3 install -r requirements.txt
Usage: python3 b64obfuscer.py path/of/source.py path/of/destination.py 
Note: source & destination must be .py file. Destination is created by the tool itself
"""

import base64
import os
import sys

try:
    cwd = os.getcwd()
    path_in = sys.argv[1]
except:
    print("Usage: python3 b64obfuscator.py path/of/source.py path/of/destination.py")
    print("Note: source & destination must be .py file. Destination is created by the tool itself.")
    sys.exit()

with open(path_in, "r", encoding='UTF-8') as content:
    code = base64.b64encode(bytes(content.read(), 'utf-8'))
    path_out = sys.argv[2]
    with open(path_out, "w") as content2:
        payload = "import base64 \nexec(base64.b64decode({}))".format(code)
        print(payload)
        content2.write(payload)

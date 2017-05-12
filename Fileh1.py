__author__ = 'kaushik'

import glob
import sys
import os

files = glob.glob("C:/Users/kaushik/*")
print (type(files))
files.sort(key=os.path.getmtime)
print("\n".join(files))

print ( sys.argv[1]
        )


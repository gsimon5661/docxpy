import fnmatch
import os
from io import BytesIO
from docxpy  import docxreader


def get_file():
    file = None
    data = None

    full_path = "/Users/mcsimon/Desktop/workspace/python/docxpy/tests/Hello.docx"
    file = open(full_path, 'rb')
    data = file.read()
    byte_stream = BytesIO(data)
    file.close()

    return byte_stream

try:
    docxreader.process("/Users/mcsimon/Desktop/workspace/python/docxpy/tests/Hello.docx")
except:
    print("1. file not found")

try:
    docxreader.process(get_file())
except:
    print("2. file not found")
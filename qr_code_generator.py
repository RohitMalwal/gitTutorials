import pyqrcode
import os

k = pyqrcode.create("Hey there")
k.png('file_name.png', scale=10)

os.system("file_name.png")

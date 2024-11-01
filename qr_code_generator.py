import pyqrcode
import os

qrcode = pyqrcode.create("Hey there")
qrcode.png('file_name.png', scale=10)

os.system("file_name.png")

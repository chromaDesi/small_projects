"""
This snippet takes in a url and creates a scannable QR code along with a desired file name of said QR Code
"""


import pyqrcode
import png
from pyqrcode import QRCode



urlInput = input("Insert URL needed to be converted: ")
fileName = input("Name the file: ")

f = f"{fileName}.png"

url = pyqrcode.create(urlInput)
url.png(f, scale = 8)

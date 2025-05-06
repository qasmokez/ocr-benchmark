from src.apple_ocr.ocr import OCR
from PIL import Image

image = Image.open("img2.JPG")
ocr_instance = OCR(image=image)

df = ocr_instance.recognize()
print(df['Content'])
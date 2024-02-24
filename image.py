from time import sleep
from PIL import ImageGrab

imagePath = "./static/images/image.jpg"

while True:
    sleep(1)
    imageFile = ImageGrab.grab()
    imageFile.save(imagePath, quality=25)
from simpleimage import SimpleImage
from PIL import Image

FILE = "images/blended_sketch.jpeg"

def new_filter():
    image = SimpleImage(FILE)

    for pixel in image:
        average = ((255 - pixel.red / 2) + (255 - pixel.green / 2) + (255 - pixel.blue / 2)) // 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    
    image.show()
    image.pil_image.save("images/background.jpeg")

if __name__ == "__main__":
    new_filter()
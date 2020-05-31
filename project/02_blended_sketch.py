from simpleimage import SimpleImage
from PIL import Image

FILE2 = "images/phoenix__sketch.jpeg"
FILE1 = "images/hope.jpg"
ALPHA = 0.85

def merging_image():
    image1 = Image.open(FILE1)
    image2 = Image.open(FILE2)

    blended_image = Image.blend(image1, image2, ALPHA)
    blended_image.show()
    blended_image.save("images/blended_sketch.jpeg")

if __name__ == "__main__":
    merging_image()


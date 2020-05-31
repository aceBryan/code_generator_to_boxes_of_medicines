from simpleimage import SimpleImage

# Global variables
FILE = "images/phoenix.jpeg"
MAXIMUM_RGB = 255
BOX_FILTER_SIZE = 11
ITERATIONS_OF_BOX_FILTERING = 13

def making_copy(filename):
    # Image properties
    image = SimpleImage(FILE)
    width = image.width
    height = image.height

    # Making a blank image
    copy_image = SimpleImage.blank(width, height)

    # Copying the image
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            copy_image.set_pixel(x, y, pixel)
    return copy_image

def grayscale(original_image):
    copy_image = making_copy(original_image)
    
    for pixel in copy_image:
        gray_value = (0.299 * pixel.red) + (0.587 * pixel.green) + (0.144 * pixel.blue)
        pixel.red = gray_value
        pixel.green = gray_value
        pixel.blue = gray_value
    
    return copy_image

def invert_color(original_image):
    image_to_invert_color = SimpleImage(FILE)

    for pixel in image_to_invert_color:
        pixel.red = MAXIMUM_RGB - pixel.red
        pixel.green = MAXIMUM_RGB - pixel.green
        pixel.blue = MAXIMUM_RGB - pixel.blue
    
    return image_to_invert_color

def boundary(x, y, width, height):
    if (x >= 0) and (width > x) and (y >= 0) and (height > y):
        return True
    return False

def blur_filter(original_image, BOX_FILTER_SIZE, ITERATIONS_OF_BOX_FILTERING):
    first_image = original_image

    for i in range(ITERATIONS_OF_BOX_FILTERING):
        blurred_image = making_copy(first_image)
        for x in range(first_image.width):
            for y in range(first_image.height):
                blurring_image(x, y, blurred_image, first_image, BOX_FILTER_SIZE)
        first_image = blurred_image
    return blurred_image

def blurring_image(x, y, blurred_image, first_image, BOX_FILTER_SIZE):
    red = 0
    green = 0
    blue = 0
    counter = 0

    r = (BOX_FILTER_SIZE - 1) // 2

    new_x_one = x - r
    new_x_two = x + r + 1
    new_y_one = y - r
    new_y_two = y + r + 1
    
    for i in range(new_x_one, new_x_two):
        for j in range(new_y_one, new_y_two):
            if boundary(i, j, first_image.width, first_image.height):
                counter += 1
                pixel = first_image.get_pixel(i, j)
                red += pixel.red
                green += pixel.green
                blue += pixel.blue
    
    pixel = blurred_image.get_pixel(x, y)
    pixel.red = red / counter
    pixel.green = green / counter
    pixel.blue = blue / counter

def calculating_sketch(maximum_value, minimum_value):
    value = (minimum_value * MAXIMUM_RGB) / max(1, MAXIMUM_RGB - maximum_value)
    return min(value, MAXIMUM_RGB)

def sketching(maximum, minimum):
    image = making_copy(maximum)
    for pixel in image:
        x = pixel.x
        y = pixel.y
        maximum_pixel = maximum.get_pixel(x, y)
        minimum_pixel = minimum.get_pixel(x, y)
        pixel.red = calculating_sketch(maximum_pixel.red, minimum_pixel.red)
        pixel.green = calculating_sketch(maximum_pixel.green, minimum_pixel.green)
        pixel.blue = calculating_sketch(maximum_pixel.blue, minimum_pixel.blue)
    return image

def main():
    original_image = SimpleImage(FILE)
    making_copy(FILE)
    
    gray_sketch = grayscale(original_image)    
    inverted_image = invert_color(original_image)
    image_blurred = blur_filter(inverted_image, BOX_FILTER_SIZE, ITERATIONS_OF_BOX_FILTERING)
    sketch = sketching(gray_sketch, image_blurred)
    sketch.show()
    sketch.pil_image.save("images/phoenix__sketch.jpeg")

if __name__ == "__main__":
    main()

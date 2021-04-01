# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("beach.jpg")

# This line attempts to open a new window to display the image.
image_original.show()

width, height = image_original.size

pixels_original = image_original.load()

r, g, b = pixels_original[100, 200]


# Don't forget to use parentheses around your (r, g, b)
pixels_original[100, 200] = (r, g, b)

image_original.save("the_file_goes_here.jpg")

# Create a new image in RGB format that is the same size as image_original
image_new = Image.new("RGB", image_original.size)
pixels_new = image_new.load()

# print(pixels_new)
pixels_new[0, 1] = (r, g, b)


image_new.show()

image_new.save("the_new_image.jpg")
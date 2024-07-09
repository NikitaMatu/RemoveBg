from rembg import remove
from PIL import Image

def remove_bg(file):
    input_image = Image.open(file)
    output_image = remove(input_image)
    output_image.save(file)
    
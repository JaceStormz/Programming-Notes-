import sys
# PIL is the library for gif files
from PIL import Image

images = []

for arm in sys.argv[1:]:
    image = image.open(arg)
    images.append(image)

image[0].save(
    "costume.gif", save_all=True, append_image=[images[1]], duration=200, loop=0
)
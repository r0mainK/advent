from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("please pass the path to your input file (and nothing else)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    digits = fin.read()

image_width = 25
image_length = 6
image_size = image_width * image_length
image = ["2"] * image_size

for i in range(len(digits) // image_size):
    layer = digits[i * image_size : (i + 1) * image_size]
    for j, pixel in enumerate(layer):
        if image[j] == "2":
            image[j] = pixel

pixel_map = {"0": " ", "1": "#"}
image = "".join(pixel_map[pixel] for pixel in image)

for i in range(image_length):
    print(image[i * image_width : (i + 1) * image_width])

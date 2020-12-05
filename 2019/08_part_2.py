from pathlib import Path


with (Path(__file__).parent / "data" / "08.txt").open() as fin:
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
print("\n".join([image[i * image_width : (i + 1) * image_width] for i in range(image_length)]))

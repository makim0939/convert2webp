import glob
import os
from PIL import Image

format = "webp"
src_dir = "src_images/"
dist_dir = "webp_images/"


def main():
    files = (
        glob.glob(src_dir + "**/*.png", recursive=True)
        + glob.glob(src_dir + "**/*.PNG", recursive=True)
        + glob.glob(src_dir + "**/*.jpg", recursive=True)
        + glob.glob(src_dir + "**/*.JPG", recursive=True)
        + glob.glob(src_dir + "**/*.jpeg", recursive=True)
        + glob.glob(src_dir + "**/*.JPG", recursive=True)
    )
    for file in files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        dir_name = dist_dir + "/".join(file.split("/")[1:-1])
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        print("convert: " + dir_name + "/" + file_name + ".webp")
        image = Image.open(file)
        image = image.convert("RGB")
        image.save(dir_name + "/" + file_name + ".webp", "webp", optimize=True)


if __name__ == "__main__":
    main()

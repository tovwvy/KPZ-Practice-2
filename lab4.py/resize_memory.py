import os.path

from PIL import Image


def resize_image(path):
    if not isinstance(path, str):
        raise Exception("There should be a string")

    image = Image.open(path)
    width, heigth = image.size
    original_size = os.path.getsize(path)

    path_resize = "image/cropped/resized.jpg"
    image.convert("L").save(path_resize)
    new_image_size = os.path.getsize(path_resize)
    wanted_size = int(original_size * 0.75)

    procent = 1
    qualityImage = 100
    while wanted_size <= new_image_size:

        image.resize((int(width*procent), int(heigth*procent)))
        image.convert("L").save(path_resize, optimize=True, quality=qualityImage)
        new_image_size = os.path.getsize(path_resize)

        qualityImage -= 1
        procent -= 0.01
    return path_resize


image = Image.open(resize_image("image/original/image.jpg"))
size = os.path.getsize("image/original/image.jpg")
resized_size = os.path.getsize("image/cropped/resized.jpg")
print ("Розмір в байтах оригінала: " + str(size) +
       "\nРозмір в байтах resized.jpg: " + str(resized_size) +
       "\nОчікуваний результат: " + str(int(size * 0.75)))

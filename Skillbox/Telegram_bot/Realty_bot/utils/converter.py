from PIL import Image
import os


def converter_webp_in_jpg(filename, path):
    extension = filename.split('.')[-1]
    f_name = filename.split('.')[0]
    img = Image.open(path + filename)
    if extension == 'webp':
        image = img.convert('RGB')
        res = path + f_name + '.jpg'
        print(res)
        image.save(res, 'jpeg')
        os.remove(path + filename)





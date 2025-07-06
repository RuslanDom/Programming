from PIL import Image
from rembg import remove

input_path = f"before_images/first_july.jpg"
out_path = f"after_images/{input_path.split('/')[1].split('.')[0]}_remove.png"

def remove_back(image: str):
    with Image.open(image) as img:
        output = remove(img)
        output.save(out_path)

print(out_path)

remove_back(input_path)
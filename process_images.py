# import time
# import os
# import concurrent.futures
# from PIL import Image, ImageFilter

# image_names = os.listdir("Threading/images")

# size = (1200, 1200)
# size_1 = (1200, 1200)

# def process_image(img_name):
#     img_path = f"Threading/images/{img_name}"
    
#     img = Image.open(img_path)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img = img.filter(ImageFilter.GaussianBlur(12))
#     img = img.filter(ImageFilter.GaussianBlur(9))
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img = img.filter(ImageFilter.GaussianBlur(12))
#     img = img.filter(ImageFilter.GaussianBlur(9))

#     img.thumbnail(size)
#     img.thumbnail(size_1)
#     img.thumbnail(size)
#     img.thumbnail(size_1)
#     img.thumbnail(size)
#     img.thumbnail(size_1)
#     img.thumbnail(size)
#     img.thumbnail(size_1)
#     img.save(f'processed/{img_name}')
    
#     print(f'{img_name} was processed...')

# if __name__ == "__main__":
#     t1 = time.perf_counter()

#     os.makedirs("processed", exist_ok=True)
#     # for image_name in image_names:
#     #     process_image(image_name)
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         list(executor.map(process_image, image_names))

#     t2 = time.perf_counter()

#     print(f'Finished in {t2-t1} seconds')







import time
import os
import concurrent.futures
from PIL import Image, ImageFilter

image_names = os.listdir("Threading/images")

size = (1200, 1200)
size_1 = (1200, 1200)

def process_image(img_name):
    img_path = f"Threading/images/{img_name}"
    
    img = Image.open(img_path)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img = img.filter(ImageFilter.GaussianBlur(12))
    img = img.filter(ImageFilter.GaussianBlur(9))
    img = img.filter(ImageFilter.GaussianBlur(15))
    img = img.filter(ImageFilter.GaussianBlur(12))
    img = img.filter(ImageFilter.GaussianBlur(9))

    img.thumbnail(size)
    img.thumbnail(size_1)
    img.thumbnail(size)
    img.thumbnail(size_1)
    img.thumbnail(size)
    img.thumbnail(size_1)
    img.thumbnail(size)
    img.thumbnail(size_1)
    img.save(f'processed/{img_name}')
    
    return f'{img_name} was processed...'

if __name__ == "__main__":
    t1 = time.perf_counter()

    os.makedirs("processed", exist_ok=True)
    # for image_name in image_names:
    #     process_image(image_name)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_image, image_name) for image_name in image_names]
    for f in futures:
        print(f.result())

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
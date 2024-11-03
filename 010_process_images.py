import time
from PIL import Image, ImageFilter

image_names = [
    'IMG_0006.JPEG',
    'IMG_0031.JPEG',
    'IMG_0034.JPEG',
    'IMG_0045.JPEG',
    'IMG_0053.JPEG',
    'IMG_0054.JPEG',
    'IMG_0063.JPEG',
    'IMG_0088.JPEG',
    'IMG_0090.JPEG',
    'IMG_0100.JPEG',
    'IMG_0130.JPEG',
    'IMG_0138.JPEG',
    'IMG_0142.JPEG',
    'IMG_0143.JPEG',
    'IMG_0147.JPEG',
    'IMG_0150.JPEG',
    'IMG_0151.JPEG',
    'IMG_0155.JPEG',
    'IMG_0157.JPEG',
    'IMG_0158.JPEG'
]

if __name__ == '__main__':

    t1 = time.perf_counter()

    size = (1200, 1200)

    for image_name in image_names:
        image = Image.open(f'raw/{image_name}')
        image = image.filter(ImageFilter.GaussianBlur(15))
        image.thumbnail(size)
        image.save(f'processed/{image_name}')
        print(f'{image_name} was processed...')
    
    t2 = time.perf_counter()

    print(f'Finished in {t2 - t1} seconds.')

# We cannot be sure if the time taken is IO bound or CPU bound.
# This is because the images are read and copied to another folder,
# so we are not entirely sure if the filter() function is the most
# resource consuming. This can be tested for a larger batch of
# images.
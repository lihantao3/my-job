import os
import glob
from PIL import Image
import threading


PREFIX = 'thumbnails'

def generate_thumbnail(infile, size, format='PNG'):
    '''生成指定格式的缩略图'''
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            threading.Thread(target=generate_thumbnail, args=(infile, (size, size))).start()


if __name__ == '__main__':
    main()

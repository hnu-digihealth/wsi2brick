from json import load

from tqdm import tqdm
import numpy as np
from openslide import OpenSlide
from skimage.color import deltaE_ciede2000, rgb2lab, lab2rgb


def convert_wsi(path_to_slide: str):
    pass


def convert_tile(slide: OpenSlide, region: tuple[int, int], size: int) -> np.array:
    region = slide.read_region(region, 0, (size, size))
    region.save('input.png')
    # refactor json to have plates as dict with ids as keys
    color_dict = load(open('src/wsi2brick/brick_sets/lego_1x1.json'))
    colors = {}
    base_plate = color_dict['base_plate']
    # conversion does not seem to to work, rgb must be in range 0-1
    colors[base_plate['id']] = rgb2lab([[[x/255 for x in base_plate['color_rgb']]]])[0][0]

    for entry in color_dict['plates']:
        colors[entry['id']] = rgb2lab([[[x/255 for x in entry['color_rgb']]]])[0][0]

    res = np.zeros([size, size])

    i = 0
    for row in tqdm(np.array(region)):
        j = 0
        for pixel in row:
            pixel = pixel[:3]
            pixel_lab = rgb2lab([[pixel]])[0][0]
            min_id = 0
            min_distance = np.inf
            for id, color in colors.items():
                distance = deltaE_ciede2000(pixel_lab, color)
                if distance < min_distance:
                    min_distance = distance
                    min_id = id
            res[i][j] = min_id
            region.putpixel((j,i), tuple([int(np.rint(x*255)) for x in lab2rgb([[colors[min_id]]])[0][0]]))
            j+=1
        i+=1

    return res, region

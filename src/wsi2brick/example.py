from sys import exit
from argparse import ArgumentParser

from PIL import Image
from openslide import OpenSlide

from wsi2brick import convert_wsi, convert_tile


def init_argparse() -> ArgumentParser:
    parser = ArgumentParser(
        prog='wsi2brick',
        description='Convert (a section of a) whole slide images to a lego mosaic'
    )
    parser.add_argument('filename', help='The whole slide image to convert', type=str)
    parser.add_argument('output', help='The output directory', type=str)
    parser.add_argument('-s', '--tile-size', help='The size of the tiles', default=32, type=int)
    parser.add_argument(
        '-m', '--mode',
        help='The mode of the conversion, should a whole wsi be converted or just a tile of it',
        choices=['wsi', 'tile'],
        default='wsi',
        type=str
    )
    parser.add_argument(
        '-r', '--region',
        help='The region to convert. Only required if mode is tile.',
        nargs=2,
        default=(0, 0),
        type=int
    )
    return parser


if __name__ == '__main__':
    parser = init_argparse()

    args = parser.parse_args()
    

    # TODO remove debug code
    print(args)

    if args.mode == 'wsi':
        pass
        #brick = convert_wsi(args.filename)
        # save wsi
    elif args.mode == 'tile':
        ids, brick = convert_tile(OpenSlide(args.filename), tuple(args.region), args.tile_size)
        print(ids)
        brick.save(args.output)


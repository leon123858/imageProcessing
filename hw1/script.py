import cv2
from argparse import ArgumentParser, Namespace
from pathlib import Path

MODE = {
    'INTER_LINEAR': cv2.INTER_LINEAR, 'INTER_CUBIC': cv2.INTER_CUBIC
}


def main(args):
    image = cv2.imread(str(args.input_path))
    cons = 1 / args.factor
    width = int(image.shape[1] * cons)
    height = int(image.shape[0] * cons)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=args.mode)
    cv2.imwrite(str(args.output_path), image)


def parse_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--mode", type=str, default='INTER_LINEAR')
    parser.add_argument("--factor", type=float, default=0.2)
    parser.add_argument("--input_path", type=Path, default="./input.jpg")
    parser.add_argument("--output_path", type=Path, default="./output.jpg")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    args.mode = MODE[args.mode]
    main(args)

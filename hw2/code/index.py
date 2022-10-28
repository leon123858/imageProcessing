from pathlib import Path
import argparse
import cv2
import matplotlib.pyplot as plt


def main(args):
    image = cv2.imread(str(args.input_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)
    cv2.imwrite(str(args.output_path / 'eqImage.png'), eq)
    # 畫出直方圖
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.savefig(
        str(args.output_path / 'originHist.png'))
    plt.clf()
    plt.hist(eq.ravel(), 256, [0, 256])
    plt.savefig(
        str(args.output_path / 'eqHist.png'))


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_path", type=Path, default="../origin.png")
    parser.add_argument("--output_path", type=Path,
                        default="../results")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)

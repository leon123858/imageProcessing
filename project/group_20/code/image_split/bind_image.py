from PIL import Image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--images_path", default='../../cache/split',
                    help='save clip image')
parser.add_argument("--cache_path", default='../../cache/bind_result.jpg',
                    help='result image')
opt = parser.parse_args()

# 讀取圖檔
crop_imgs = []
for i in range(9):
    crop_imgs.append(Image.open(opt.images_path +
                     "/frame{}.jpg".format(str(i))))

w, h = crop_imgs[0].size

target = Image.new('RGB', (w * 3, h * 3))
for row in range(3):
    for col in range(3):
        # 对图片进行逐行拼接
        # paste方法第一个参数指定需要拼接的图片，第二个参数为二元元组（指定复制位置的左上角坐标）
        # 或四元元组（指定复制位置的左上角和右下角坐标）
        target.paste(crop_imgs[3*row+col], (0 +
                     w*col, 0 + h*row))
target.save(opt.cache_path, quality=100)  # 成品图保存

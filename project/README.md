# style transfer

## init env

_suggest python>=3.8_

```shell
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
pip install torchfile
pip install opencv-python
pip install Pillow
pip install gdown
pip install --upgrade --no-cache-dir gdown
```

## download data

```shell
# in root of this project
gdown https://drive.google.com/uc?id=19f-dXPq-M00nkRZwa81V6VeZdavgbm5N
unzip -o IP_sampleData.zip
gdown https://drive.google.com/uc?id=19flUPvhE0aMrVFlqWka8dwdleumv6_us
unzip -o IP_models.zip
```

## methods

### 影片拆成 frames

```python
parser.add_argument("--video_dir", default='../../sampleData/video_0.mp4',
                    help='video path')
parser.add_argument("--cache_dir", default='../../cache/frames',
                    help='frames saved path')
```

```shell
# setDir('/libs/video2frames')
python video2frames.py --video_dir='../../sampleData/video_1.mp4' --cache_dir='../../cache/frames'
```

### frames 合成影片

```python
parser.add_argument("--frames_dir", default='../../cache/frames',
                    help='frames path')
parser.add_argument("--cache_dir", default='../../cache',
                    help='video saved path')
```

```shell
# setDir('/libs/video2frames')
python frames2video.py
```

### 圖片轉換

- 放內容圖片的資料夾,contentPath: ../../sampleData/
- 放風格圖片的地方,stylePath: ../../styleImage/
- 取哪層,layer: r41 or r31
- 結果放哪,outf: ../../cache/
- 輸出圖片像素,fineSize:1024

```shell
# setDir('/libs/style_transfer')
!python TestArtistic.py --layer='r41' --vgg_dir='../../models/vgg_r41.pth' --decoder_dir='../../models/dec_r41.pth' --matrixPath='../../models/r41.pth' --stylePath='../../styleImage/' --contentPath='../../sampleData/' --outf='../../cache/' --fineSize='1024'
```

### 影片轉換

- 放內容圖片的資料夾,content_dir: ../../cache/frames/
- 放風格圖片的地方,style: ../../styleImage/in2.jpg
- 取哪層,layer: r41 or r31
- 結果放哪,outf: ../../cache/frames/
- 輸出圖片像素,fineSize:1024

```shell
# setDir('/libs/style_transfer')
!python TestVideo.py --style=../../styleImage/27.jpg
```

## Sample

```shell
cd ./libs/video2frames
# 把範例影片拆成圖片
python video2frames.py

cd ../style_transfer
# 把範例圖片和所有風格資料夾內圖片做風格轉換
python TestArtistic.py
# 把每一張範例影片的圖片做風格轉換
python TestVideo.py

cd ../video2frames
# 把每一張範例影片的圖片(轉換後)合成回影片
python video2frames.py
```

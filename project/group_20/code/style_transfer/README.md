## Learning Linear Transformations for Fast Image and Video Style Transfer

**[[Rewrite From]](https://github.com/sunshineatnoon/LinearStyleTransfer)**

## Init env

**note: suggest python>=3.8**

use this script

```shell
!pip install opencv-python
!pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
!pip install torchfile
!pip install gdown
```

or just use this shell
`bash set_env.sh`

## install trained model

use command where you want

```shell
gdown https://drive.google.com/uc?id=19flUPvhE0aMrVFlqWka8dwdleumv6_us
unzip -o IP_models.zip
```

## 用法

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

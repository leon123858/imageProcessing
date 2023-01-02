# 分割生成高畫質圖片實驗

## 環境

**note: suggest python>=3.8**

use this script

```shell
!pip install opencv-python
```

## 流程

把圖片拆開
參數

```python
'''
參數
parser.add_argument("--image_path", default='../../sampleData/image_1.jpg',
                    help='image path')
parser.add_argument("--cache_dir", default='../../cache/split',
                    help='save clip images')
'''
python split_image.py
```

圖片合成

```python
'''
參數
parser.add_argument("--images_path", default='../../cache/split',
                    help='save clip image')
parser.add_argument("--cache_path", default='../../cache/bind_result.jpg',
                    help='result image')
'''
python bind_image.py
```

# 影片圖片轉換

## 環境

**note: suggest python>=3.8**

use this script

```shell
!pip install opencv-python
```

## 流程

把影片拆成圖片
參數

```python
'''
參數
parser.add_argument("--video_dir", default='../../sampleData/video_0.mp4',
                    help='video path')
parser.add_argument("--cache_dir", default='../../cache/frames',
                    help='frames saved path')
'''
python video2frames.py
```

圖片合成

```python
'''
參數
parser.add_argument("--frames_dir", default='../../cache/frames',
                    help='frames path')
parser.add_argument("--cache_dir", default='../../cache',
                    help='video saved path')
'''
python frames2video.py
```

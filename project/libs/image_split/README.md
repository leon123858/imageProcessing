# 分割生成高畫質圖片實驗

## 流程

把圖片拆開
`python split_image.py`

影片風格轉換(進入 style transfer 資料夾)
`python TestVideo.py --fineSize=1024 --content_dir=../../cache/split --style=../../styleImage/27.jpg`

圖片合成
`python bind_image.py --images_path=../../cache/frames`

## 結論

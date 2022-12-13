# 分割生成高畫質圖片實驗

## 流程

把圖片拆開
`python split_image.py`

影片風格轉換(進入 style transfer 資料夾)
`python TestVideo.py --fineSize=1024 --content_dir=../../cache/split --style=../../styleImage/27.jpg`

圖片合成
`python bind_image.py --images_path=../../cache/frames`

## 結論

效果不錯, 但須更精確的處理影像拼接,
此外, 無法無限制拉大, 因為第一次運算生成的濾鏡只是無數塊圖中的一小片, 所以切太小片效果就會在其他塊不好

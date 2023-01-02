# Team 20 Process Image Final Project

## Project Structure

Code 資料夾下每一個資料夾都是一組腳本, 利用各個腳本排列組合, 可以實做出所有功能
各腳本環境配置與細節操作, 詳見各自內部的 README

## 各組腳本說明

- CCPL
  利用此組腳本, 可以訓練 CCPL 模型, 並用其風格轉換圖片與影片
- image_split
  利用此組腳本, 可以把一張圖片切割成多張小圖片, 或多張切割的小圖片合成回一張原始圖片
- style_transfer
  利用此組腳本, 可以利用 LinearStyleTransfer 模型風格轉換圖片與影片
- video2frames
  利用此組腳本, 可以把影片拆成多個幀, 或把多多個幀合成為一部影片

## Sample

詳見個資料夾內 README.md

```shell
cd ./code/video2frames
# 把範例影片拆成圖片
python video2frames.py

cd ../style_transfer
# 利用 linear style transfer 完成圖片影片轉換
python TestArtistic.py
python TestVideo.py

cd ../CCPL
# 利用 CCPL 完成圖片影片轉換
python test.py --content input/content/lenna.jpg --style input/style/in2.jpg --decoder <decoder_dir> --SCT <SCT_dir> --testing_mode <artistic or photo-realistic>
python test_video_frame.py --content_dir <video frames dir> --style_path input/style/in2.jpg --decoder <decoder_dir> --SCT <SCT_dir> --testing_mode <artistic or photo-realistic>

cd ../video2frames
# 把每一張範例影片的圖片(轉換後)合成回影片
python video2frames.py
```

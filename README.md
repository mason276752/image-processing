# 粉專/IG圖文加工器

## 介紹
* 給PS智障(ex:我)使用，用於產生圖文
* 腳本省去每次重複步驟
* 可載入圖片(方形，請先處理過，歡迎PR)
* 圖片簡易套用濾鏡
* 可將圖片切片

## 要求
* Python 版本 3.9

## 安裝
* 安裝最新 python
* `pip3 install -r requirement.txt`

## 效果
![](./square_example.png)
![](./fb_example.png)
![](./ig_example.jpeg)

## 範例
```
./square.sh
./fb_w2_3_h1_1_1.sh
./ig_w1_1_1_h1_1_1_1.sh
```

## 簡易說明
* 不設定邊框(border)顏色就不會有邊框
* 不代入 bgimage 預設純白背景

### FB 預覽說明
FB 會偵測人臉會使得圖片預覽位置偏易，拼圖對不上。<br />
建議用景物圖，或經過高斯模糊處理。

### mode: 處理對象
0. 一大圖
1. 2:1
2. 3:2
3. 1:2
4. 2:3
5. 四格圖

## LICENSE
MIT
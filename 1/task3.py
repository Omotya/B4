import cv2
import matplotlib.pyplot as plt

img_path1 = "/home/student/School/test/newcomer/1/matigai1.png"
img_path2 = "/home/student/School/test/newcomer/1/matigai2.png"

# 画像表示関数
def show(img,path):
    plt.figure(figsize=(10, 10))
    plt.imshow(img, vmin = 0, vmax = 255)
    plt.savefig(path)
    plt.show()
    plt.close()

# 画像読み込み
img1 = cv2.imread(img_path1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread(img_path2)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


# 画像の差分

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=2)

##差分マスクの計算
fgmask = fgbg.apply(img1)
fgmask = fgbg.apply(img2)
show(fgmask,"image/差分マスク.png")

##画像を暗くして差分マスクを重ねる
img1 = img1 // 4
img1[fgmask==255] = (255, 0, 0)
show(img1,"image/差分.png")

cv2.waitKey(0)

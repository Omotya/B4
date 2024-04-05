import cv2

image1 = cv2.imread("/home/student/School/test/newcomer/1/cat.png")
image2 = cv2.imread("/home/student/School/test/newcomer/1/cat.png", 0)


# 画像の表示
cv2.imshow("test1", image1)

#画像の拡大(サイズを指定する)
h,w = image1.shape[:2]
result1 = cv2.resize(image1, (w*2, h))
cv2.imwrite('image/result1.png', result1)

#画像の縮小(縦横の倍率を指定)
result2 = cv2.resize(image1, None, fx=1/2, fy=1)
cv2.imwrite('image/result2.png', result2)

#画像の回転
result3 = cv2.rotate(image1, cv2.ROTATE_90_CLOCKWISE)
result4 = cv2.rotate(image1, cv2.ROTATE_90_COUNTERCLOCKWISE)
result5 = cv2.rotate(image1, cv2.ROTATE_180)

cv2.imwrite('image/result3.png', result3)
cv2.imwrite('image/result4.png', result4)
cv2.imwrite('image/result5.png', result5)

#2値化
threshold = 100

cv2.imwrite('image/image2.png', image2)
ret, result6 = cv2.threshold(image2, threshold, 255, cv2.THRESH_BINARY)
ret, result7 = cv2.threshold(image2, 0, 255, cv2.THRESH_OTSU)
print("ret: {}".format(ret))

cv2.imwrite('image/result6.png', result6)
cv2.imwrite('image/result7.png', result7)

cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)

import cv2
import matplotlib.pyplot as plt

img1_path= "/home/student/School/test/newcomer/1/tomato.png"
img2_path= "/home/student/School/test/newcomer/1/sea.png"


def show_img(path,outpath1,outpath2):
    img = cv2.imread(path)
    b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]
    hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
    hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
    hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
    plt.plot(hist_r, color='r', label="r")
    plt.plot(hist_g, color='g', label="g")
    plt.plot(hist_b, color='b', label="b")
    plt.legend()
    plt.savefig(outpath1)
    plt.show() 
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = img2[:,:,0], img2[:,:,1], img2[:,:,2]
    hist_h = cv2.calcHist([h],[0],None,[256],[0,256])
    hist_s = cv2.calcHist([s],[0],None,[256],[0,256])
    hist_v = cv2.calcHist([v],[0],None,[256],[0,256])
    plt.plot(hist_h, color='r', label="h")
    plt.plot(hist_s, color='g', label="s")
    plt.plot(hist_v, color='b', label="v")
    plt.legend()
    plt.savefig(outpath2)
    plt.show()

    return hist_r,hist_g, hist_b, hist_h, hist_s, hist_v

r,g,b,h,s,v = show_img(img1_path,"image/rgb1.png","image/hsv1.png")
r,g,b,h,s,v = show_img(img2_path,"image/rgb2.png","image/hsv2.png")

# img1 = cv2.imread(img1_path)
# surf = cv2.xfeatures2d.SURF_create(400)
# kp, des = surf.detectAndCompute(img,None)
# len(kp)
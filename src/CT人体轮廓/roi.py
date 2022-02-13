import cv2
from PIL import Image
import numpy as np
import os

folder = os.path.split(__file__)[0]
inputfile = folder + "/CT_heart_float32_flip.raw"

data = np.fromfile(inputfile,dtype=np.float32) # 利用numpy加载二进制文件，加载之后是一个一维数组，array类型
data = np.reshape(data,[70,70,50]) # reshape成实际三维大小
data = data/np.max(data) # 归一化

# DEBUG code:
# img = data[:,:,25]
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL) 
# cv2.imshow("Image", img)

def floodfill(im_th):
    # Copy the thresholded image.
    # im_th = cv2.UMat(im_th)
    # im_th = cv2.adaptiveThreshold(im_th, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0)
    # im_th = cv2.cvtColor(im_th, cv2.COLOR_GRAY2BGR)
    # im_th = cv2.cvtColor(im_th, cv2.COLOR_BGR2GRAY)
    a = Image.fromarray(im_th)
    a.save("tmp.png")
    im_th = cv2.imread("tmp.png",1)
    os.remove("tmp.png")
    im_th = cv2.cvtColor(im_th, cv2.COLOR_BGR2GRAY)
    im_floodfill = im_th.copy()
    
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    
    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv

    kernel = cv2.getGaussianKernel(ksize = 5, sigma = 3)
    im_out = cv2.erode(im_out,kernel,iterations = 3)
    im_out = cv2.dilate(im_out,kernel,iterations = 3)
    
    return im_th,im_floodfill,im_floodfill_inv,im_out

def get_roi(nslice, th):
    img = data[:,:,nslice]
    mask = img > th/256.0
    im_th,im_floodfill,im_floodfill_inv,im_out = floodfill(mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    erode = cv2.erode(im_out, kernel,iterations=1)
    dilate = cv2.dilate(erode, kernel,iterations=1)
    dilate = cv2.dilate(dilate, kernel2,iterations=3)
    mask = mask.astype(np.float32)
    # DEBUG code:
    # new = np.concatenate([img,im_th,im_floodfill,im_floodfill_inv,im_out],axis=1)
    # cv2.imshow("Image", new) 
    return im_out

def refresh(nslice, th):
    img = data[:,:,nslice]
    mask = img > th/256.0
    im_th,im_floodfill,im_floodfill_inv,im_out = floodfill(mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    erode = cv2.erode(im_out, kernel,iterations=1)
    dilate = cv2.dilate(erode, kernel,iterations=1)
    dilate = cv2.dilate(dilate, kernel2,iterations=3)
    print(type(dilate))
    # print(dilate.type)
    mask = mask.astype(np.float32)
    new = np.concatenate([img,im_th,im_floodfill,im_floodfill_inv,im_out],axis=1)
    cv2.imshow("Image", new) 

def trackThreshold(x):
    nslice = cv2.getTrackbarPos("Slice", "Image") 
    refresh(nslice,x)

def trackSlice(x):
    th = cv2.getTrackbarPos("Threshold", "Image") 
    refresh(x,th)

refresh(20,12)

cv2.createTrackbar("Threshold", "Image", 1, 256, trackThreshold)
cv2.createTrackbar("Slice", "Image", 1, 49, trackSlice)

cv2.waitKey (0) 
cv2.destroyAllWindows()

#  write the roi

roi = np.zeros([70,70,50]).astype(np.int32)

for i in range(data.shape[2]):
    img = get_roi(i, 56)
    roi[:,:,i] = img.astype(np.bool).astype(np.int32)

roi.tofile(folder + "/ROI_CT_heart_int32_flip.raw")
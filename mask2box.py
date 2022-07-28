import os
import cv2
import numpy as np

data_dir = '/home/mikrestenitis/Databases/Bios Dataset/'
save_dir = '/home/mikrestenitis/Databases/Bios Dataset/boxes'
os.makedirs(save_dir, exist_ok=True)

mask_img_filename = 'ID_00087_UAV_dji.phantom.4.pro.hawk.1_[Lat=39.54193311304993,Lon=22.644217169634043,Alt=4.800000190734863]_DATE_03_07_2019_14_39_58.png'

mask = cv2.imread(os.path.join(data_dir, 'labels', mask_img_filename))
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
rgb_img =  cv2.imread(os.path.join(data_dir, 'images', mask_img_filename))

# -- Threshold img -- #
ret, mask_bin = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)

# -- Detect contours -- #
contours_list, hierarchy = cv2.findContours(mask_bin,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

# -- Draw bounding box -- #
for i,c in enumerate(contours_list):
    # contour1 = cv2.drawContours(rgb_img, contours_list, i, (255, 0, 255), 3)
    x, y, w, h = cv2.boundingRect(c)
    M = cv2.moments(c)
    if M['m00'] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        color = mask[cY, cX]
        color = (int(color[0]), int(color[1]), int(color[2]))
        cv2.rectangle(rgb_img, (x, y), (x + w, y + h), tuple(color), 5)

cv2.imwrite(os.path.join(save_dir, mask_img_filename), rgb_img)
#ssh 22f3000652@se2001.ds.study.iitm.ac.in

import cv2
import numpy as np


resolution_x = 500
resolution_y = 500

pic = np.zeros((resolution_x, resolution_y))

print(repr(pic))

cv2.imwrite("picture2.png", pic)
import numpy as np
import cv2
# import matplotlib.pyplot as plt
import os

def Clahe(in_path,i):
	# in_path='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\r12'
	out_path='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\r100L_out'
	# img = cv.imread(path)
	# # print('img',img.shape)
	# print('img',img.shape)
	# # create a CLAHE object (Arguments are optional).
	# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	# cl1 = clahe.apply(img)
	# # cl1 = cv.cvtColor(cl1, cv.COLOR_BGR2RGB)
	# # print('cl1',cl1.shape)
	# cv.imshow('clahe_1.jpg',cl1)
	# cv.waitKey(0)
	# res = np.hstack((img, cl1))

	# cv.imwrite('clahe_1.jpg',cl1)

	# path_li = os.listdir(in_path)
	# print(path_li)
	# i=1
	# for file in path_li:

	# filename = os.path.join(in_path,file)
	bgr = cv2.imread(in_path)

	lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

	lab_planes = cv2.split(lab)

	clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

	lab_planes[0] = clahe.apply(lab_planes[0])

	lab = cv2.merge(lab_planes)

	bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

	results = os.path.join(out_path,'clahe'+str(i)+'_in'+'.png')
	print(results)
	# cv2.imshow('clahe.png',bgr)
	cv2.imwrite(results,bgr)
	# cv2.waitKey(0)
		# i+=1


# if __name__=="__main__":
# 	Clahe(in_path,i)		

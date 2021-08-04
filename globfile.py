import cv2
from clahe import Clahe
import os
import glob

root_dir ='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\Rain100L\\'
out_path='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\r100L_gt'
in_path = 'C:\\Users\\HanHan\\RainTrainH\\h'
gt_path ='C:\\Users\\HanHan\\RainTrainH\\h_gt'

rain = os.listdir(in_path)
gt = os.listdir(gt_path)

print(rain)
print(gt)
# root_dir needs a trailing slash (i.e. /root/dir/)
# for filename in glob.iglob(root_dir + '**/*.txt', recursive=True):
# i=1
# for filename in glob.glob(os.path.join(root_dir, '**\\40000_out.png'), recursive=True):
	# Clahe(filename,i)
	# i+=1
	# print(filename)
	# results = os.path.join(out_path,str(i)+'_GT'+'.png')
	# print(results)
	# img = cv2.imread(filename)
	# cv2.imshow('clahe.png',bgr)
	# cv2.imwrite(results,img)
	# i+=1
	# print(filename)


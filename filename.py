import os
import glob
import numpy as np
import random
import re

#input和label圖片沒有對到時可以用
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

path_input='E:\\han\\Didmdn-test\\label'
# path_label='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\result_image\\gt28'
# in_path = 'C:\\Users\\HanHan\\derain_dataset\\rainy_image_dataset\\rainy_image_dataset\\training\\input'
# gt_path ='C:\\Users\\HanHan\\srresnet-edge-enhance-swt-resnet-final\\create_h5_dataset-master\\create_h5_dataset-master\\result_image\\gt28'
path_li = os.listdir(path_input)
path_li.sort(key=natural_keys)
# path = os.listdir(gt_path)
# path.sort(key=natural_keys)
# print(path_li)
# print(path)
# print(path_li[0].split('.')[0].split('-')[1])	
# print(path_li[0].split('.')[0].split('-')[1]==path[0].split('.')[0].split('-')[1])
# index=[]
# indexs=[]
# i=1
# for file in path:
# 		index.append(file.split('.')[0].split('-')[1])
# print(len(index))
# for files in path_li:
# 		indexs.append(files.split('.')[0].split('-')[1])
# print(len(indexs))
# diff = list(list(set(indexs)-set(index)))
# # a=diff.sort(key=natural_keys)
# # diff = sorted(diff, reverse=True)
# # print(diff)
# # print(type(diff))
# print(len(diff))

# for i in range(0, len(diff)): 
#     diff[i] = int(diff[i])
# diff = sorted(diff, reverse=False)
# print(diff)
# print(len(diff))

# file_paths=[]
# with open('test1200.txt', 'w') as f:#把路徑寫成txt檔
#     for item in path_li:
#         filepath = os.path.join(path_input, item)
#         print(filepath)
#         file_paths.append(filepath)
#     for path in file_paths:             
        
#         f.write("%s\n" % path)

count=1
for filename in path_li:
    
#     #new_name = str(count)
    # print(filename)
    # os.rename(os.path.join(path_input,filename), os.path.join(path_input,filename.split('_')[0]+'_'+'training'+'.png'))
    # os.rename(os.path.join(path_label,filename), os.path.join(path_label,new_name+'_in'+'.png'))
    # os.rename(os.path.join(path_li,filename), os.path.join(path_li,'gt_'+filename.split('.')[0]+'.jpg'))
    os.rename(os.path.join(path_input,filename), os.path.join(path_input,filename.split('.')[0]+'_GT'+'.jpg'))


    # int(count)
    count+=1
print(count)
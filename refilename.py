import os
import glob
import numpy as np
import random
import re
import cv2

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


#path_input='C:\\Users\\HanHan\\TIP17_\training_code\\rain13000\\input'
path_label='C:\\Users\\HanHan\\derain_dataset\\sys_rain_14\\mask\\m1'
# input_path='C:\\Users\\HanHan\\TIP17_training_code\\rainy_image_dataset\\rainy_image_dataset\\training\\aug_label'

# path_li = os.listdir(path_input)
path_li = os.listdir(path_label)
path_li.sort(key=natural_keys)
print((path_li))

#count=1
# for filename in path_li:

    
    # new_name = str('%03d'%count)
    # img_name = filename[i].split('.')[0]
    #os.rename(os.path.join(path_input,filename), os.path.join(path_input,new_name+'_in'+'.png'))
    # os.rename(os.path.join(path_label,filename), os.path.join(path_label,filename.split('.')[0]+'.png'))

    #int(count)
    #count+=1

# path_li = os.listdir(path_input)    
# print((path_li))
 
input_path='C:\\Users\\HanHan\\RainTrainH\\h_gt'
path = os.listdir(input_path)
path.sort(key=natural_keys)
print('path:',path)
# for i in range(len(path)):
    # print(path[i])
    # if((i+1)%70==0):
    #     # print('nnnnn:',i+1)
    #     print((path[i]))


# j=1
# i=0
# for filename in path:
#     img = cv2.imread(input_path+'\\'+path[i])
#     img_name = path[i].split('.')[0]
#     # print(input_path+'\\'+path[i])
#     # print('img_name:',img_name)
#     # file_name = input_path+'/'+img_name+'_'+str(j+1)+'.png'
#     # for j in range(num_image):
#     os.rename(os.path.join(input_path,filename), os.path.join(input_path,img_name.split('_')[0]+'_'+str(j)+'.jpg'))
#     j=j+1
#     if(j>14):
#         j=1
#     i=i+1

    # file_name = log_path+'/'+img_name.split('_')[0]+'_'+str(j+1)+'.jpg'
    # print(file_name)
    # cv2.imwrite(file_name,img)    
    
    
    
    
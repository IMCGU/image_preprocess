import os 
import glob
import time
import cv2

def check_img(img):
    cv2.imshow('__DEBUG__',img)
    cv2.waitKey(0)

def build_log_dir(name):
    """Set up a timestamped directory for results and logs for this training session"""
    if name:
        log_path = name  # (name + '_') if name else ''
    else:
        log_path = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_path = os.path.join('result_image', log_path)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    return log_path

if __name__ == '__main__':
    input_path_G = 'C:\\Users\\HanHan\\derain_dataset\\rainy_image_dataset\\rainy_image_dataset\\training\\label'
    #input_path_T = 'D:\\han\\create_h5_dataset-master\\VAL_112\\rain'
  
    num_ground_T = 28

    dir_data_G = os.listdir(input_path_G)
    #dir_data_T = os.listdir(input_path_T)

    # print(sorted(dir_data_G)[0])
    # print(sorted(dir_data_T)[0])
    log_path = build_log_dir('gt28')
    #print(input_path_G)
    #print(dir_data_G)
    
    for i in range(len(dir_data_G)):
        img = cv2.imread(input_path_G+'\\'+dir_data_G[i])
        # check_img(img)
        img_name = dir_data_G[i].split('.')[0]
        #img_name = dir_data_G[i].split('_')[0]
        print(input_path_G+'\\'+dir_data_G[i])
        for j in range(num_ground_T):
            file_name = log_path+'/'+img_name+'_'+str(j+1)+'.jpg'
            # file_name = log_path+'/'+img_name.split('_')[0]+'_'+str(j+1)+'.jpg'
            print(file_name)
            cv2.imwrite(file_name,img)
    
 

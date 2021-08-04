
from util_han import *
# import tensorflow as tf
import argparse
from BatchThread_t3 import ThreadedGenerator
import time
import multiprocessing
import h5py
import os 
import glob
from tqdm import tqdm,trange


def process_data_set(iterator_train,iterator_label, iterator_mask, batch_idx,path,process_type,img_size = 96,random_crop=False):
    iteration = 0
    pool = multiprocessing.Pool(2)
    #bar = tqdm(iterator)
    iterator_train = iter(iterator_train)
    iterator_label = iter(iterator_label)
    iterator_mask = iter(iterator_mask)
    
    #t = trange(batch_idx,ncols=100)
    pbar = tqdm(range(batch_idx),bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
    for i in pbar:
        pbar.set_description("Process...")
        data_train = next(iterator_train)
        data_label = next(iterator_label)
        data_mask = next(iterator_mask)
        
        #process_time_start = time.time()
        results_train = pool.map(imread, data_train)
        results_label = pool.map(imread, data_label)
        results_mask = pool.map(imread, data_mask)

        #tqdm.write('[Process Time: %4.4f]' % (time.time() - process_time_start))
        batch_train = np.asarray(results_train)
        batch_label = np.asarray(results_label)
        batch_mask = np.asarray(results_mask)
        
        process_loop_time_start = time.time()

        tmp_train = []
        tmp_label = []
        tmp_mask = []

        for j in range(len(batch_train)):
            
            try:

                img_train, img_label, img_mask = process_sub_image(batch_train[j],batch_label[j],batch_mask[j],img_size=img_size,random_crop=random_crop)
                # checkimage(img_train)
                # checkimage(img_label)
                print(j)
                #print('looping..')
                tmp_train.append(img_train)
                tmp_label.append(img_label)
                tmp_mask.append(img_mask)
            except:
                continue
        # tqdm.write('[Time: %f]' % (time.time() - process_loop_time_start))
        #print("[-------_______doing_______-------]: %s"% iteration)    
        tmp_train = np.asarray(tmp_train)
        tmp_label = np.asarray(tmp_label)
        tmp_mask = np.asarray(tmp_mask)
        #print(tmp_.shape)
        iteration += 1
        
            
        with h5py.File(path, 'a') as hf:
            #print(os.path.join(os.getcwd(),path))
            if iteration == 1:
                #print('not')
                hf.create_dataset(process_type, data=tmp_train, compression="gzip", chunks=True, maxshape=(None,img_size,img_size,3)) 
                hf.create_dataset('label', data=tmp_label, compression="gzip", chunks=True, maxshape=(None,img_size,img_size,3)) 
                hf.create_dataset('mask', data=tmp_mask, compression="gzip", chunks=True, maxshape=(None,img_size,img_size,3)) 
                #hf.create_dataset("train", data=tmp_, maxshape=(None))
            hf[process_type].resize((hf[process_type].shape[0] + tmp_train.shape[0]), axis = 0)
            hf[process_type][-tmp_train.shape[0]:] = tmp_train

            hf['label'].resize((hf['label'].shape[0] + tmp_label.shape[0]), axis = 0)
            hf['label'][-tmp_label.shape[0]:] = tmp_label

            hf['mask'].resize((hf['mask'].shape[0] + tmp_mask.shape[0]), axis = 0)
            hf['mask'][-tmp_mask.shape[0]:] = tmp_mask

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--is-val', action='store_true')
    parser.add_argument('--is-train', action='store_true')
    parser.add_argument('--is-eval', action='store_true')
    parser.add_argument('--train-dir', type=str, help='Directory containing training images')
    parser.add_argument('--label-dir', type=str, help='Directory containing label images')
    parser.add_argument('--mask-dir', type=str, help='Directory containing mask images')
    parser.add_argument('--val-dir', type=str, default='Benchmarks/', help='Directory containg imagrs for validation')
    parser.add_argument('--val-label-dir', type=str, default='Benchmarks/', help='Directory containg imagrs for validation label')    
    parser.add_argument('--val-mask-dir', type=str, default='Benchmarks/', help='Directory containg imagrs for validation mask')    
    # parser.add_argument('--eval-dir', type=str, default='Benchmarks/', help='Directory containg imagrs for validation')
    # parser.add_argument('--eval-label-dir', type=str, default='Benchmarks/', help='Directory containg imagrs for validation label')
    parser.add_argument('--batch-size', type=int, default=16, help='Mini-batch size.')
    parser.add_argument('--img-size', type=int, default=96, help='Mini-batch size.')
    args = parser.parse_args()
      
    train_filenames, label_filenames, mask_filenames, \
    val_filenames, val_label_filenames, val_mask_filenames,\
    eval_filenames, eval_label_filenames, eval_mask_filenames = input_setup(args)
    
    print(len(train_filenames))
    print(len(val_filenames))
    
    if args.is_train:
        train_iter = ThreadedGenerator(train_filenames , args.batch_size, random_crop=True)
        label_iter = ThreadedGenerator(label_filenames , args.batch_size, random_crop=True)
        mask_iter = ThreadedGenerator(mask_filenames , args.batch_size, random_crop=True)
        #path = 'PreprocessedData.h5'
        path ='12600ps_24.h5'
        iterator_train_batch = train_iter
        iterator_label_batch = label_iter
        iterator_mask_batch = mask_iter
        process_type = 'train'

        batch_idx = len(train_filenames) // args.batch_size
        
        
        
        random_crop = True
        process_data_set(iterator_train_batch, iterator_label_batch, iterator_mask_batch, batch_idx, path, process_type ,img_size=args.img_size ,random_crop=random_crop)

    
    if args.is_val:
        val_iter = ThreadedGenerator(val_filenames, args.batch_size, random_crop=True)
        val_label_iter = ThreadedGenerator(val_label_filenames, args.batch_size, random_crop=True)
        val_mask_iter = ThreadedGenerator(val_mask_filenames, args.batch_size, random_crop=True)
        #path = 'PreprocessedData_val.h5'
        path = '112ps_val.h5'
        iterator_train_batch = val_iter
        iterator_label_batch = val_label_iter
        iterator_mask_batch = val_mask_iter

        process_type = 'val'
        batch_idx = len(val_filenames) // args.batch_size
        random_crop = True
        process_data_set(iterator_train_batch, iterator_label_batch, iterator_mask_batch, batch_idx, path, process_type ,img_size=args.img_size ,random_crop=random_crop)

    if args.is_eval:
        eval_iter = ThreadedGenerator(eval_filenames, args.batch_size, random_crop=True)
        eval_label_iter = ThreadedGenerator(eval_label_filenames, args.batch_size, random_crop=True)
        eval_mask_iter = ThreadedGenerator(eval_mask_filenames, args.batch_size, random_crop=True)
        path = 'PreprocessedData_eval_24.h5'
        iterator_train_batch = eval_iter
        iterator_label_batch = eval_label_iter
        iterator_mask_batch = eval_mask_iter

        process_type = 'eval'
        batch_idx = len(eval_filenames) // args.batch_size
        random_crop = True
        process_data_set(iterator_train_batch, iterator_label_batch, iterator_mask_batch, batch_idx, path, process_type ,img_size=args.img_size ,random_crop=random_crop)

    # if args.is_eval:
    #     eval_iter = ThreadedGenerator(eval_filenames, args.batch_size, random_crop=False)    
    #     eval_label_iter = ThreadedGenerator(eval_labe_filenames, args.batch_size, random_crop=False)    
    #     # iterator_batch = eval_iter
    #     iterator_train_batch = eval_iter
    #     iterator_label_batch = eval_label_iter
    #     path = 'PreprocessedData_eval.h5'
    #     process_type = 'eval'
    #     batch_idx = len(eval_filenames) // args.batch_size
    #     random_crop = False

    
    print('*******************************************')
    print('training files locations: %s'%args.train_dir)
    print('validation files locations: %s'%args.val_dir)
    print('batch-size: %s '%args.batch_size)
    print('image size: %s '%args.img_size)    
    
    print('*******************************************')
    print('training files locations: %s'%args.train_dir)
    print('validation files locations: %s'%args.val_dir)
    print('batch-size: %s '%args.batch_size)
    print('image size: %s '%args.img_size)  

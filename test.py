#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
#author:davidtu  
#FileName: *.py  
#Version:1.0.0  
#====#====#====#====

import pickle
import sys
default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)

# sys.setdefaultencoding(default_encoding)

input_dir = "D:/imagerecognitionTensorFlowAlexnet/Ubuntu/src/dataset_1MM/"
# input_dir = "README.md"
W_fname = "W.pkl"
dataset_fname = "dataset.pkl"
with open(input_dir + dataset_fname, mode="rb") as f:
    # f1 = f.readlines()
    train_data, val_data, test_data = pickle.load(f, encoding="bytes")
    # for i in f.readline():
    #     print(i)
# print(f1)
tmp_filename2 = input_dir + "/" + W_fname
with open(tmp_filename2, 'rb') as f:
    W, _ = pickle.load(f, encoding='bytes')


# print(W2[])
print("done")

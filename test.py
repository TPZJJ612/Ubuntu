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

input_dir = "D:/ReadBehavioursLog/ubottu/src/dataset_1MM/W.pkl"
# input_dir = "README.md"
# W_fname = ""

with open(input_dir, mode="rb") as f:
    # f1 = f.readlines()
    W, W2 = pickle.load(f, encoding="bytes")
    # for i in f.readline():
    #     print(i)
# print(f1)

print(W2[])
print("done")

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 07:30:24 2023

@author: Heng2020
"""

import modeling_tool as ml
import torch

num_gpus = torch.cuda.device_count()

if num_gpus > 0:
    print(f"Number of GPUs available: {num_gpus}")
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No GPU available.")

def check_gpu(verbose = 1):
    import torch
    num_gpus = torch.cuda.device_count()

    if num_gpus > 0:
        if verbose >= 1:
            print(f"Number of GPUs available: {num_gpus}")
        for i in range(num_gpus):
            if verbose >= 1:
                print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        if verbose >= 1:
            print("No GPU available.")
    return num_gpus

check_gpu()


import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')

if len(physical_devices) > 0:
    print("GPUs available:")
    for device in physical_devices:
        print(device)
else:
    print("No GPU available.")
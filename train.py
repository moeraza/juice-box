import sys, os
sys.path.insert(0, "./src/modeling")


from ssd import *
from yolov3 import *
from yolov5 import *
from rcnn import *


#### User Defined Vars ####

# Model Selection
yolov3  = True
yolov5  = True
rcnn    = True
ssd     = True

# Model Agnostic Options
pretrained_weights      = True # start from pre trained weights
save_model_weights      = True
save_performance_report = True

# Dev options
sample  = True # only use a small sample of data for testing
epochs  = 5


#### Model Run ####


if yolov3:
    train_yolov3(save_model_weights)

if yolov5:
    train_yolov5(save_model_weights)

if rcnn:
    train_rcnn(save_model_weights)

if ssd:
    train_ssd(save_model_weights)



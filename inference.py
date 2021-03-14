import sys, os
sys.path.insert(0, "./src/modeling")


from ssd import *
from yolov3 import *
from yolov5 import *
from rcnn import *
import datetime

date_stamp = str(datetime.datetime.now())


# Model Selection
yolov3  = True
yolov5  = True
rcnn    = True
ssd     = True



# Model Agnostic Options
save_img = False
generate_box = True



#### Model Inference ####


if yolov3:
    output = inference_yolov3()
    if save_img:
        output.save("./inferences/yolov3_{0}.jpg".format(date_stamp))

if yolov5:
    output = inference_yolov5()
    if save_img:
        output.save("./inferences/yolov5_{0}.jpg".format(date_stamp))

if rcnn:
    output = inference_rcnn()
    if save_img:
        output.save("./inferences/rcnn_{0}.jpg".format(date_stamp))

if ssd:
    output = inference_ssd()
    if save_img:
        output.save("./inferences/ssd_{0}.jpg".format(date_stamp))


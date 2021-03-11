# Juice Box
Waste Disposal Method Rec Sys

Juice Box uses deep learning methods to develop an easy-to-use solution where an Ontario residence can take a picture of their waste and have an appropriate waste deispol method recomended to them based on their region.


# Getting started

#### Requirements 

To install the required python packages simply type
```bash
$ pip3 install -r requirements.txt
```

#### Train Model 

To re-train model on images in data folder and update weights
```bash
$ python train.py
```

#### Generate Inference 

To generate an inference on an img
```bash
$ python inference.py path/to/img.jpg
```
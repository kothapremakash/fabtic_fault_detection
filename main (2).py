import cv2
import tensorflow
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

def run(source = None):

    model = tensorflow.keras.models.load_model('E:/Final year project/Final year project/FABRIC - Copy/FABRIC - Copy/model/weights_best.hdf5')

    img = cv2.imread(source)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(img_gray, (5, 5), 0)   
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    img_half = cv2.resize(img, (255, 255))
    img_half = cv2.cvtColor(img_half, cv2.COLOR_BGR2GRAY)
    x = img_to_array(img_half)
    x = np.array(x).reshape(-1, 255, 255, 1)

    y_pred = model.predict(x)
#     y_pred
    if y_pred >= 0.5:
        y_pred = 0
        return "The Fabric is Defect."
    else:
        y_pred = 1
        return "The Fabric is good."

    
# run(source='C:\Users\12016\Desktop/FABRIC - Copy/Defect/aug_0_10.png')

if __name__ == "__main__":
    # opt = parse_opt()
    # main(opt)
    run(source='C:/Users/12016/Desktop/FABRIC - Copy/Defect/aug_0_10.png')

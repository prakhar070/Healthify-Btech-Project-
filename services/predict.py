import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
from PIL import Image
from keras import backend as K
from keras.models import load_model
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os

# Any results you write to the current directory are saved as output.
#MEDIA_ROOT = os.path.join(BASE_DIR,"media")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def predict_result(file):  
    image_path = BASE_DIR+file
    model_path = BASE_DIR+"/services/my_model.h5"
    image = cv2.imread(image_path)
    image = cv2.resize(image, (50,50)) 
    image_arr = np.array(image)
    image_arr = np.expand_dims(image_arr, axis=0)
    model = load_model(model_path)
    out = model.predict(image_arr)
    K.clear_session()
    if out[0][0] < out[0][1] :
        ret = 1
    else:
        ret = 0
    return ret        
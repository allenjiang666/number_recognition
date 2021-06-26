from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import load_model
from sfl_demo import app
import secrets
import os


def save_picture(form_picture):
    # Generate file name to avoid same file name
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/sketches', picture_fn)

    #resize upload file to save space
    output_size = (28,28)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn,picture_path
    
def predict_picture(picture_path):
    img = Image.open(picture_path)
    img = img.convert('L')
    img =255- np.asarray(img).copy()
    img_format = img.reshape(-1,784)
    #normalize the input data
    img_normal = img_format/255
    mlp = load_model('my_model.h5')
    prediction = int(mlp.predict_classes(img_normal)[0])
    return prediction
       


  




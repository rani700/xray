from flask import Flask,request, render_template
import numpy as np 
import matplotlib.pyplot as plt
import json
from werkzeug import secure_filename
from keras.models import load_model
from keras import backend as keras
import cv2
import base64



def dice_coef(y_true, y_pred):
    y_true_f = keras.flatten(y_true)
    y_pred_f = keras.flatten(y_pred)
    intersection = keras.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1) / (keras.sum(y_true_f) + keras.sum(y_pred_f) + 1)

def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)



model = load_model('model.h5', custom_objects={'dice_coef_loss':                   
dice_coef_loss, 'dice_coef': dice_coef})



app = Flask(__name__)
# CORS(app)

@app.route('/',methods=['GET' , 'POST'])
def index():

  if request.method == 'POST':
      f = request.files['file']
      f.save("static/"+secure_filename(f.filename))

      if f.filename.split('.')[-1] == 'jpeg':
        img_path ="static/"+secure_filename(f.filename)
        X_shape=512
        x_im = cv2.resize(cv2.imread(img_path),(X_shape,X_shape))[:,:,0]
        op = model.predict((x_im.reshape(1, 512, 512, 1)-127.0)/127.0)
        
        plt.imshow(x_im, cmap="bone", label="Input Image")
        plt.savefig('static/frame/'+secure_filename(f.filename))

        plt.imshow(x_im, cmap="bone", label="Output Image")
        plt.imshow(op.reshape(512, 512), alpha=0.5, cmap="jet")
        plt.savefig('static/mask/'+secure_filename(f.filename))


      return render_template('dashboard.html', img = secure_filename(f.filename))
      # return df[:100].to_html()

  if request.method == 'GET':
      return render_template('upload.html')
  
    



if __name__ == "__main__":
  app.run(threaded=False)
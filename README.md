# Lung fields segmentation on chest X-ray images
Build and trained a deep learning model (UNet Model) Using a dataset on kaggle  

Training Model [train.ipynb](https://github.com/rani700/xray/blob/master/train.ipynb)  
Testing [test.ipynb](https://github.com/rani700/xray/blob/master/test.ipynb)  
Trained Model file [model.h5](https://github.com/rani700/xray/blob/master/model.h5)  
  
Testing on live notebook [Test on Google colab](http://colab.research.google.com/github/rani700/xray/blob/master/test.ipynb) <i>Open this Google Colab link run the cells upload the xray image from the dataset. And check out the segmented image generated.</i>  
For testing [These images can be used](https://github.com/rani700/xray/tree/master/images)  
  
## Flask Application
I also have build a web interface where you can upload x-ray image and it will generate its 
segementation and display it to you.
I had decided to host it on heroku but unfortunately its slug size increased due to Tensorflow, Keras, OpenCV depencdencies  
  
### The application is locally  
#### Steps to run locally
```
git clone https://github.com/rani700/xray.git
cd xray
python main.py
open http://127.0.0.1:8000/
```

Upload the xray image and the it will display the input (x-ray) and output (segmented x-ray) on the webpage.  

  
### Screenshots
<img src="https://github.com/rani700/xray/blob/master/screenshots/UI1.png?raw=true" />
<img src="https://github.com/rani700/xray/blob/master/screenshots/UI2.png?raw=true" />
<img src="https://github.com/rani700/xray/blob/master/screenshots/UI3.png?raw=true" />


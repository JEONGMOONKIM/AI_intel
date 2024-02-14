
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model


img_path='../datasets/horse-or-human/test02.jpg'
model_path='./horse_or_human_1.0.h5'

model=load_model(model_path)

img=Image.open(img_path)
img=img.convert('RGB')
img=img.resize((64,64))
data=np.asarray(img)
data=data/255
data=data.reshape(1,64,64,3)

pred=model.predict(data)
print(pred)







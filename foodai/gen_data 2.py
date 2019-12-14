from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ["cabbage", "carrot", "japaneseradish", "onion", "tomato"]
num_classes = len(classes)
image_size = 50

#画像の読み込み

X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)
xy = (X_train, X_test, y_train, y_test)
np.save("./food.npy", xy)
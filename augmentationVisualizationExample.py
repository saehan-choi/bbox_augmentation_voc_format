import cv2
import os
from utils import transform
import shutil
import albumentations as A
import matplotlib.pyplot as plt

YouWillHaveToRemove = []
listImage = os.listdir('./train/train_images/')

for i in listImage:
    imgPath   = f'./train/train_images/{i}'
    labelPath = f'./train/train_labels/{i[:-4]}.txt'
    ResultPath = f'./augmentation/labels/aug_{i[:-4]}.txt'    
    
    try:
        img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
        f = open(labelPath, 'r')
        f = f.readlines()

        # print(imgPath)

        for k in f:
            k = k.split()
            x1, y1, x2, y2 = int(k[1]), int(k[2]), int(k[3]), int(k[4])
            imgTrim = img[y1:y2, x1:x2]
            height, width = imgTrim.shape[0], imgTrim.shape[1]

            transformedImg = transform(imgTrim, width, height)
            img[y1:y2, x1:x2] = transformedImg

        cv2.imwrite(f'./augmentation/images/aug_{i}',img)
        shutil.copy(labelPath, ResultPath)

    
    except:
        # 여기서 만들어진거 지워버려야 나중에 편함
        YouWillHaveToRemove.append(i[:-4])
        print(i)
        pass

print(YouWillHaveToRemove)
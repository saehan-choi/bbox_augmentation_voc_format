import cv2

imgPath   = './train/train_images/0_Parade_marchingband_1_5.jpg'
labelPath = './train/train_labels/0_Parade_marchingband_1_5.txt'


img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

f = open(labelPath, 'r')
f = f.readlines()

for k in f:
    k = k.split()
    x1, y1, x2, y2 = int(k[1]), int(k[2]), int(k[3]), int(k[4])
    # print(img.shape)
    print(f'{x1} {y1} {x2} {y2}')
    img = cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
# 0_Parade_marchingband_1_5

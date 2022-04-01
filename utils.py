import albumentations as A
import cv2

def transform(img, width, height):
    transform = A.Compose([
        A.RandomCrop(width=round(width*0.8),height=round(height*0.8),p=0.5),
        A.HorizontalFlip(p=0.8),
        A.RandomBrightnessContrast(p=0.8)
        ])

    transformed = transform(image=img)
    transformedImg = transformed["image"]
    transformedHeight, transformedWidth = transformedImg.shape[0], transformedImg.shape[1]

    if transformedWidth != width or transformedHeight != height:
        transformedImg = cv2.resize(transformedImg, (width,height), interpolation=cv2.INTER_CUBIC)

    return transformedImg
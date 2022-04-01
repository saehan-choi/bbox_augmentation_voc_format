# bbox_augmentation_voc_format 
WIDERFace Dataset

![image](https://user-images.githubusercontent.com/70372577/161203238-8bf8928f-ffb4-4b36-beb7-90a3cc994abe.png)

![image](https://user-images.githubusercontent.com/70372577/161203396-20ddd3e9-3a5d-42a7-b291-e8fcf20a08e7.png)

![image](https://user-images.githubusercontent.com/70372577/161203266-5292e659-83f0-4ece-8918-22cb3680d2fa.png)

![image](https://user-images.githubusercontent.com/70372577/161203301-636b37b5-f822-4b3e-969b-0ec634a2f2aa.png)

if you wanna add something, you can add different things in albumentations library

    transform = A.Compose([
        A.RandomCrop(width=round(width*0.8),height=round(height*0.8),p=0.5),
        A.HorizontalFlip(p=0.8),
        A.RandomBrightnessContrast(p=0.8)
        ])

file structure

![image](https://user-images.githubusercontent.com/70372577/161204367-0f2e7d4b-b2fb-4369-8c30-2bacd59e725e.png)

ex) example.txt
    ->  0 x1 y1 x2 y2
    ->  0 x1 y1 x2 y2...


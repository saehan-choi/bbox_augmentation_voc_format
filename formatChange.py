import os

# k = os.listdir('./train/train_labels/')
result_path = './train/train_labels/'
k = open('./wider_train.txt', 'r')

k = k.readlines()

for a in k:
    a = a.split()
    print(a)
    if len(a) == 1:
        print(result_path+a[0]+'.txt')
        f = open(result_path+a[0]+'.txt', 'w')
    
    else:
        x1, y1, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])
        x1_, y1_, x2_, y2_ = x1, y1, x1+w, y1+h
        f.write(f'0 {x1_} {y1_} {x2_} {y2_}\n')
        print(f'0 {x1_} {y1_} {x2_} {y2_}')
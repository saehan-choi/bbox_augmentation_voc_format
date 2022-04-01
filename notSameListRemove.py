import os
from collections import Counter



arr = []
train_images = os.listdir('./train/train_images/')
train_labels = os.listdir('./train/train_labels/')


# Counter쓰면 되겠다 두개 append시키고

for i in train_images:
    arr.append(i[:-4])

for j in train_labels:
    arr.append(j[:-4])


print(Counter(arr).most_common()[-5:])

# 여기서 제일작은수의 갯수 알수있음




# print(train_images)
# print(train_labels)

# for i in train_images:
#     for j in train_labels:

#         if i[:-4] == j[:-4]:
#             print(i)
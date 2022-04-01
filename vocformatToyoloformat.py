import os

# 여기에 print로 나와진 이미지, 라벨들 제거하기
arr = ['12_Group_Large_Group_12_Group_Large_Group_12_31', '29_Students_Schoolkids_Students_Schoolkids_29_230', '2_Demonstration_Demonstration_Or_Protest_2_202', '2_Demonstration_Demonstration_Or_Protest_2_520', '2_Demonstration_Demonstration_Or_Protest_2_543', '2_Demonstration_Demonstration_Or_Protest_2_546', '2_Demonstration_Demonstration_Or_Protest_2_666', '2_Demonstration_Demonstrators_2_206', '2_Demonstration_Demonstrators_2_373', '2_Demonstration_Demonstrators_2_559', '2_Demonstration_Political_Rally_2_444', '2_Demonstration_Political_Rally_2_71', '2_Demonstration_Protesters_2_346', '33_Running_Running_33_660', '35_Basketball_basketballgame_ball_35_805', '35_Basketball_Basketball_35_102', '35_Basketball_Basketball_35_220', '36_Football_americanfootball_ball_36_184', '36_Football_Football_36_63', '39_Ice_Skating_iceskiing_39_380', '46_Jockey_Jockey_46_576', '46_Jockey_Jockey_46_717', '48_Parachutist_Paratrooper_Parachutist_Paratrooper_48_258', '48_Parachutist_Paratrooper_Parachutist_Paratrooper_48_283', '7_Cheering_Cheering_7_17']

ImgPath = './augmentation/images/'
labelPath = './augmentation/labels/'

print()


for i in arr:
    try:
        os.remove(ImgPath+'aug_'+i+'.txt')
        os.remove(labelPath+'aug_'+i+'.jpg')
    except:
        pass

    # os.remove(ImgPath+i)


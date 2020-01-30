import os 
import shutil

list1 = os.listdir("training")

for f in list1:
    os.chdir('C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training\\')
    list2 = os.listdir(f)
    os.chdir('C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training\\'+str(f))
    for i in list2:
        str1 = i
        if "seg" in str1:
            src = str(i)
            shutil.move(src, "C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training seg")
            
            
    os.chdir('..')    
    
for f in list1:
    os.chdir('C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training\\')
    list2 = os.listdir(f)
    os.chdir('C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training\\'+str(f))
    for i in list2:
        list3 = os.listdir(i)
        os.chdir('C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training\\'+str(f)+"\\"+str(i))
        for k in list3:
            str1 = k
            if "seg" in str1:
                src = str(k)
                shutil.move(src, "C:\\Users\\boltuzamaki\\Desktop\\AI Exibition\\Deep Lab Image segmentation\\ADE20K_2016_07_26\\images\\training seg")
            
        os.chdir('..') 
    os.chdir('..')            
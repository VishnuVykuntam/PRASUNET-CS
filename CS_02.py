from PIL import Image
import numpy as np
import random

#Selecting image, replace yi.jpg with image name or provide path if in different directory/folder

image=Image.open("yi.jpg")
imageArray=np.array(image)

#encoding using random
# use seed property of random if need to encode on one machine and decode on another

encode=[]
for i in range(256):
    x=random.randint(0,255)
    while(x in encode):
        x=random.randint(0,255)
    if x not in encode:
        encode.append(x)
print(encode)

#coding the image

codedArray=np.copy(imageArray)
print("image encoding\n\n")
for i in range(256):
    codedArray[imageArray==i] = encode[i]
coded=Image.fromarray(codedArray)
coded.save("coded.jpg")

#decoding the image

decodedArray=np.copy(codedArray)
print("image decoding\n\n")
for i in range(256):
    decodedArray[codedArray==encode[i]] = i
decoded=Image.fromarray(decodedArray)
decoded.save("decoded.jpg")
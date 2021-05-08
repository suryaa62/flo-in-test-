import numpy as np 
from PIL import Image
import os, cv2


def delete_images(data_dir, username, userid):
    for imgid in range(100):
        if(os.path.exists(f"{data_dir}/{username}_{userid}_{imgid}.jpg")):
            os.remove(f"{data_dir}/{username}_{userid}_{imgid}.jpg")



def train_classifier(data_dir, username , userid):
    path = []
    for i in range(100):
        if(os.path.exists(f"{data_dir}/{username}_{userid}_{i}.jpg")):
            path.append(os.path.join(data_dir,f"{username}_{userid}_{i}.jpg"))
    

    faces = []
    ids = []

    for image in path:
        # print(image)
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')

        faces.append(imageNp)
        ids.append(1)
    
    ids = np.array(ids)

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write(f"classifiers/{username}_{userid}.xml")

    delete_images(data_dir,username,userid)


if(__name__ == '__main__'):
    username = input("Enter user name: ")
    userid = input("Enter user id: ")
    train_classifier("data",username,userid)


import cv2

"""
saves the image in data folder.
name of the image file is in the format -> username_userid_imgid.jpg
"""
def generate_dataset(img,username,userid,imgid):
    cv2.imwrite(f"data/{username}_{userid}_{imgid}.jpg",img)


def draw_boundary_around_face(img, classifier, scaleFactor, minNeighbors, color, text):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords


def save_face(img, faceCascade,username,userid,imgid):
    coordinates = draw_boundary_around_face(img,faceCascade,1.1,10,(255,0,0),username)

    if len(coordinates)==4:
        # Updating region of interest by cropping image
        roi_img = img[coordinates[1]:coordinates[1]+coordinates[3], coordinates[0]:coordinates[0]+coordinates[2]]
        # img_id to make the name of each image unique
        generate_dataset(roi_img, username, userid, imgid)

    return img


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def register_user(username,userid):
    video_capture = cv2.VideoCapture(0)
    for imgid in range(100):
        _ , img = video_capture.read()

        img = save_face(img, faceCascade, username, userid, imgid)

        cv2.imshow("User registration", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    video_capture.release()
    cv2.destroyAllWindows()

if(__name__ == '__main__'):
    username = input("Enter user name: ")
    userid = input("Enter user id: ")
    register_user(username,userid)


import cv2
import numpy as np
import matplotlib.pyplot as plt


# extract pre-trained face detector
def face_cropper(filepath, outpath,i):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    # load color (BGR) image
    img = cv2.imread(filepath)
    # convert BGR image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find faces in image
    print(filepath,end="")
    faces = face_cascade.detectMultiScale(gray)

    # print number of faces detected in the image
    print('\r{}image: {} Number of faces detected {}'.format(filepath,i,len(faces)))

    # get bounding box for each detected face
    counter = 1
    for (x, y, w, h) in faces:
        # add bounding box to color image
#        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        y0 = y-40
        if (y0 < 0):y0 = 0
        y1 = y+h+40
        if (y1 > np.shape(img)[0]):y1 = np.shape(img)[0]

        x0 = x - 40
        if (x0 < 0):x0 = 0
        x1 = x + w + 40
        if (x1 > np.shape(img)[1]):x1 = np.shape(img)[1]

        crop_img = img[y0:y1, x0:x1]
        cv2.imwrite("{}/IMG{}_{}.png".format(outpath,i,counter), crop_img)
        counter+=1



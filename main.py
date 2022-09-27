import uuid            # universal unique identifier is a python library which help to generate the random object of 128  bits 
import cv2
from retinaface import RetinaFace
import os 
import time 

def cropsavefaces(path_to_folder):

    start = time.time()

    for images in os.listdir(path_to_folder):
        print(images)
        #check if the image ends with .png or .jpg or .jpeg
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            #print(images)

            img = cv2.imread(os.path.join(path_to_folder,images))
            print("______",os.path.join(path_to_folder,images))
            resp = RetinaFace.detect_faces(os.path.join(path_to_folder,images))
            print(resp.keys())  #key method returns a view object 
            try:
                for idx,face_id in enumerate(list(resp.keys())):
                    boxes = resp[face_id]['facial_area']
                    print(boxes)
                    bbox = [(boxes[0],boxes[1],boxes[2],boxes[3])]

                    #px,py = 50,50
                    #if boxes[1] and boxes[0]>50:
                        #faces = img[boxes[1]-px:boxes[3] +50, boxes[0]-py:boxes[2]+50]
                    #else:

                    faces = img[boxes[1]:boxes[3], boxes[0]:boxes[2]]

                    #cv2.rectangle (img,(boxes[0],boxes[1]),(boxes[2],boxes[3]),color = (0,255,0),thickness=3,lineType=cv2.LINE_AA)

                    #to save the file in the folder

                    save_path  = r'D:\retina\output'
                    filename = 'crop'+str(uuid.uuid4()) +'.jpg'

                    #cv2.imshow("frame,faces")
                    #cv2.waitkey(0)

                    cv2.imwrite(os.path.join(save_path,filename),faces)

            except Exception as e:
                print(e)
                pass

    end = time.time()

    print("the time of execution of above programe is :",(end-start)*10**3,"ms")
    print("task is done")


cropsavefaces(path_to_folder=r"D:\retina\input")




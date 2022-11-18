import cv2
import numpy as np
from PIL import Image

class CV():


    vid = None
    colors = None
    frame = None
    world_coordinates = np.zeros([3,3])
    camera_coordinates = np.zeros([2,2])
    X, Y, Z = None, None, None
    x, y = None, None

    def __init__(self, vid, colors, frame):
        self.vid = vid
        self.colors = colors
        self.frame = frame
        self.X = self.world_coordinates[0]
        self.Y = self.world_coordinates[1]
        self.Z = self.world_coordinates[2]
        self.x = self.camera_coordinates[0]
        self.y = self.camera_coordinates[1]

    def capture_video(self):
        video_path = 'INSERT VIDEO PATH HERE'
        self.vid = cv2.VideoCapture(video_path)
        if not self.vid.isOpened():
            print('Camera Cannot Open')
            exit()
        while True:
            ret, frame = self.vid.read()
            frame = cv2.cvtColor(self.vid, cv2.COLOR_BGR2RGB)
            pixImage = Image.fromarray(frame)
            img = np.asarray(pixImage)
            if not ret:
                print('Cannot recieve frame. Exiting...')
                break
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', grey)
            if cv2.waitKey(1) == ord('q'):
                break
        

    def end_video(self):
        self.vid.release()
        cv2.destroyAllWindows()


    def get_RGB_values(self):
        B = self.frame[0]
        G = self.frame[1]
        R = self.frame[2]
         

    # def pinhole_model(self):




        # while True:
        #     # Reads the frame of the camera 
        #     ret, frame = self.cap.read()

        #     # shows the image with the name 'frame'
        #     cv2.imshow('frame', frame)

        #     # waitKey(0) infinitely waits until a key is pressed to end the feed 
        #     # Need to double check this implementation with the '0'
        #     if cv2.waitKey(0) == ord('e'):
        #         break

        #     self.end_video()
        
    

    # def get_RGB_values(self):
        # 


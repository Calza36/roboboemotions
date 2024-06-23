from robobopy.Robobo import Robobo
from robobopy_videostream.RoboboVideo import RoboboVideo
import cv2

#The IP must be that shown in the Robobo app
videoStream = RoboboVideo("192.168.1.177")
rob = Robobo("192.168.1.177")

def main():
    print("Starting test app")
    #Connect to the robot and start the video stream
    rob.connect()
    rob.startStream()

    videoStream.connect()

    print("Showing images")

    while True:
        cv2_image = videoStream.getImage()
        cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
        cv2.imshow('imagen', cv2_image)
        cv2.waitKey(1)

main()
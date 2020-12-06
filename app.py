import cv2
import time

cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')


def Simulator():
    CarVideo = cv2.VideoCapture('cars.mp4')
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        detection = cars_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 9)
        if(len(detection) > 0):
            print("Detected object at " + str(CarVideo.get(cv2.CAP_PROP_POS_MSEC) / 1000) + " second")
            time.sleep(2)
        controlkey = cv2.waitKey(1)
        if controlkey == ord('q'):
            break
        
    CarVideo.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Simulator()
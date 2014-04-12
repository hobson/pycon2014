import cv2

from heli import Heli

class Tracker(object):
    """TBD PID feedback control loop and video image tracking"""
    pass

def main():
    vc = cv2.VideoCapture(0)
    tracker = Tracker()
    h = Heli()
 
    while True:
        rval, frame = vc.read()
        if not rval:
            break
 
        tracker.handle_frame(frame)
        h.correct_drift(tracker)
 
        if cv2.waitKey(20) == 27:
            break
    h.land()

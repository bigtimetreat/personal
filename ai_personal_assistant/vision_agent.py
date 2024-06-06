import cv2
import numpy as np
from PIL import ImageGrab

def capture_screen():
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    cv2.imshow("Screen", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

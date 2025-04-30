import cv2
import numpy as np
from PIL import ImageGrab

def screenRecorder():
    fourcc = cv2.VideoWriter.fourcc(*'XVID')

    # my laptop resolution is 2560x1600 - Dell G16 (make sure to change this according to your laptop resolution.) 5.0 is the frame rate it will capture the screen.
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (2560, 1600))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", frame)
        out.write(frame)

        # 27 is the code for key Q on the keyboard
        if cv2.waitKey(1) == 27:
            break

    out.release()
    cv2.destroyAllWindows()

screenRecorder()

# this will output a .avi file. now let's see what's inside
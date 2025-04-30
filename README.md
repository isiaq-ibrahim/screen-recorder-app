# 🖥️ Screen Recorder App - Python

This repository contains the code for my simple yet powerful **Screen Recorder App** I built using Python. The program captures my laptop screen in real-time and saves it as an `.avi` video file.

## 📌 Features

- 📹 Real-time screen capture
- 🎥 Outputs `.avi` video format using `XVID` codec
- 🖼️ Supports high-resolution recordings (e.g., 2560x1600)
- 💻 Uses OpenCV, PIL, and NumPy for screen grabbing and video writing

## 🛠️ Technologies Used

- Python 3.10.7
- OpenCV (`cv2`)
- Pillow (`PIL`)
- NumPy

## 💡 How It Works

The script uses `PIL.ImageGrab` to take screenshots of the screen and then writes the frames into a video using `cv2.VideoWriter`.

## 📷 Sample Code

```python
import cv2
import numpy as np
from PIL import ImageGrab

def screenRecorder():
    fourcc = cv2.VideoWriter.fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (2560, 1600))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", frame)
        out.write(frame)

        if cv2.waitKey(1) == 27:  # Press 'Esc' key to stop
            break

    out.release()
    cv2.destroyAllWindows()

screenRecorder()
```

### ⚠️ Note

Make sure to adjust the screen resolution (2560, 1600) in the script to match your own display for optimal recording.

### 📄 License

This project is licensed under the MIT License.

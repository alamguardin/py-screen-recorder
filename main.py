import mss
import cv2
import numpy as np
import time

videoFrames = []
startTime = time.time()

with mss.mss() as sct:
    monitor = sct.monitors[1]

    print("Grabando pantalla... Presiona Ctrl+C para detener.")

    try:
        while True:
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            videoFrames.append(frame)
        
    except KeyboardInterrupt:
        print("Grabación finalizada.")
        endTime = time.time()
        realFps = len(videoFrames) / (endTime - startTime)
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter("output.avi", fourcc, realFps, (monitor["width"], monitor["height"]))
        
        for frame in videoFrames:
            out.write(frame)
        
        out.release()
        cv2.destroyAllWindows()

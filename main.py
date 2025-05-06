import mss
import cv2
import numpy as np

with mss.mss() as sct:
    monitor = sct.monitors[2]  # Pantalla principal
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (monitor["width"], monitor["height"]))

    for _ in range(100):  # graba 100 frames (~5 segundos a 20fps)
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        out.write(frame)

    out.release()

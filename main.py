import mss
import cv2
import numpy as np
import time

with mss.mss() as sct:
    monitor = sct.monitors[1]  # Pantalla principal
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (monitor["width"], monitor["height"]))

    print("Grabando pantalla... Presiona Ctrl+C para detener.")

    try:
        prev_time = time.time()
        while True:
            frame_start = time.time()
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            out.write(frame)
            frame_end = time.time()
            elapsed = frame_end - frame_start
            time_to_wait = max(0, (1 / 20.0) - elapsed)
            time.sleep(time_to_wait)
    except KeyboardInterrupt:
        print("Grabación finalizada.")
        out.release()
        cv2.destroyAllWindows()

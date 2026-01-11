import socket

DEVICE_ID = socket.gethostname()

import time
import os
from camera import capture_image
from logger import log_event

def lock_system():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def monitor():
    print("Monitoring agent started...")

    while True:
        # TEMPORARY trigger (simulated unauthorized access)
        time.sleep(300)

        image_path = capture_image()
        log_event(
    "UNAUTHORIZED_ACCESS",
    {
        "device_id": DEVICE_ID,
        "image": image_path
    }
)
        lock_system()

if __name__ == "__main__":
    monitor()

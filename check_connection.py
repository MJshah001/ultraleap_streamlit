# check_connection.py
import time
import Leap

ctr = Leap.Controller()

print("Service connected?", ctr.is_connected)
print("Devices found:", [d for d in ctr.devices])

prev_id = -1
for i in range(20):
    frame = ctr.frame()
    print(f"Loop {i:02d}: frame.id = {frame.id}")
    prev_id = frame.id
    time.sleep(0.25)

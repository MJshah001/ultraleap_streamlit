# import time
# import math
# import csv
# import Leap
# import numpy as np
# import streamlit as st
# from datetime import datetime

# # ---------------- Setup logging ----------------
# # Create a unique filename with the current timestamp
# start_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
# log_file = f"experiment_{start_ts}.csv"

# # Write CSV header
# with open(log_file, "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["timestamp","frame","movement","hand","value"])

# # Buffer for log rows
# log_buffer = []
# last_flush = time.time()

# # -------------- Leap + Streamlit Init --------------
# rad2deg = lambda r: r * 180.0 / math.pi
# controller = Leap.Controller()

# st.title("UltraLeap Live Hand‑Tracking Dashboard")
# movement = st.selectbox("Select movement to display", ["Pitch", "Yaw", "Roll"])

# rad_ph = st.empty()
# deg_ph = st.empty()
# hands_ph = st.empty()
# chart = st.line_chart()
# chart_buffer = []

# # ---------------- Main Loop ----------------
# while True:
#     frame = controller.frame()
#     hands = frame.hands

#     if not hands.is_empty:
#         hand = hands[0]
#         side = "Left" if hand.is_left else "Right"

#         # compute raw & degree values
#         raw = {
#             "Pitch": hand.direction.pitch,
#             "Yaw":   hand.direction.yaw,
#             "Roll":  hand.palm_normal.roll
#         }
#         deg  = {k: rad2deg(v) for k, v in raw.items()}
#         r = raw[movement]
#         d = deg[movement]

#         # update live metrics
#         rad_ph.metric(f"{movement} (rad)", f"{r:.3f}")
#         deg_ph.metric(f"{movement} (°)",   f"{d:.1f}")
#         hands_ph.metric("Hand", side)

#         # update live chart (last 100 points)
#         chart_buffer.append(d)
#         if len(chart_buffer) > 100:
#             chart_buffer.pop(0)
#         chart.add_rows({movement: np.array(chart_buffer)[-1:].reshape(1,)})

#         # log this data point with real timestamp
#         now = datetime.now().isoformat(timespec="milliseconds")
#         log_buffer.append([now, frame.id, movement, side, d])

#     # flush log_buffer to CSV every 5 seconds
#     if time.time() - last_flush >= 5 and log_buffer:
#         with open(log_file, "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerows(log_buffer)
#         log_buffer.clear()
#         last_flush = time.time()

#     time.sleep(0.03)


# import time
# import math
# import csv
# import Leap
# import numpy as np
# import streamlit as st
# from datetime import datetime
# import sys
# import atexit

# # ---------------- Setup logging ----------------
# start_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
# log_file = f"experiment_{start_ts}.csv"

# # Write CSV header
# with open(log_file, "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["timestamp","frame","movement","hand","value"])

# log_buffer = []
# last_flush = time.time()

# # Ensure final flush on exit
# def flush_on_exit():
#     if log_buffer:
#         with open(log_file, "a", newline="") as f:
#             csv.writer(f).writerows(log_buffer)
# atexit.register(flush_on_exit)

# # -------------- Leap + Streamlit Init --------------
# rad2deg = lambda r: r * 180.0 / math.pi
# controller = Leap.Controller()

# st.title("UltraLeap Live Hand‑Tracking Dashboard")
# movement = st.selectbox("Select movement to display", ["Pitch", "Yaw", "Roll"])

# # Add an Exit button
# if st.button("🔴 Exit"):
#     st.warning("Flushing data and exiting…")
#     flush_on_exit()
#     st.stop()  # stops Streamlit execution

# # Placeholders
# rad_ph   = st.empty()
# deg_ph   = st.empty()
# hands_ph = st.empty()
# chart    = st.line_chart()
# chart_buffer = []

# # ---------------- Main Loop ----------------
# while True:
#     frame = controller.frame()
#     hands = frame.hands

#     if not hands.is_empty:
#         hand = hands[0]
#         side = "Left" if hand.is_left else "Right"

#         # compute raw & degree values
#         raw = {
#             "Pitch": hand.direction.pitch,
#             "Yaw":   hand.direction.yaw,
#             "Roll":  hand.palm_normal.roll
#         }
#         deg  = {k: rad2deg(v) for k, v in raw.items()}
#         r = raw[movement]
#         d = deg[movement]

#         # update live metrics
#         rad_ph.metric(f"{movement} (rad)", f"{r:.3f}")
#         deg_ph.metric(f"{movement} (°)",   f"{d:.1f}")
#         hands_ph.metric("Hand", side)

#         # update live chart (last 100 points)
#         chart_buffer.append(d)
#         if len(chart_buffer) > 100:
#             chart_buffer.pop(0)
#         chart.add_rows({movement: np.array(chart_buffer)[-1:].reshape(1,)})

#         # log this data point with real timestamp
#         now = datetime.now().isoformat(timespec="milliseconds")
#         log_buffer.append([now, frame.id, movement, side, d])

#     # flush log_buffer to CSV every 5 seconds
#     if time.time() - last_flush >= 5 and log_buffer:
#         with open(log_file, "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerows(log_buffer)
#         log_buffer.clear()
#         last_flush = time.time()

#     time.sleep(0.03)

## belows adds hand grab strength for hand open and close detection
# import time
# import math
# import csv
# import atexit
# from datetime import datetime

# import Leap
# import numpy as np
# import streamlit as st

# # ---------------- Setup logging ----------------
# start_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
# log_file = f"experiment_{start_ts}.csv"

# # Write CSV header
# with open(log_file, "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["timestamp", "frame", "movement", "hand", "value"])

# log_buffer = []
# last_flush = time.time()

# def flush_on_exit():
#     """Flush any remaining log_buffer to disk on exit."""
#     if log_buffer:
#         with open(log_file, "a", newline="") as f:
#             csv.writer(f).writerows(log_buffer)
#         log_buffer.clear()

# atexit.register(flush_on_exit)

# # -------------- Leap + Streamlit Init --------------
# rad2deg = lambda r: r * 180.0 / math.pi
# controller = Leap.Controller()

# st.title("UltraLeap Live Hand‑Tracking Dashboard")

# # Movement dropdown now includes grab strength
# movement = st.selectbox(
#     "Select measurement to display",
#     ["Pitch", "Yaw", "Roll", "Grab Strength"]
# )

# # Exit button
# if st.button("🔴 Exit"):
#     st.warning("Flushing data and exiting…")
#     flush_on_exit()
#     st.stop()

# # Placeholders for live display
# rad_ph   = st.empty()
# deg_ph   = st.empty()
# hands_ph = st.empty()
# chart    = st.line_chart()

# chart_buffer = []

# # ---------------- Main Loop ----------------
# while True:
#     frame = controller.frame()
#     hands = frame.hands

#     if not hands.is_empty:
#         hand = hands[0]
#         side = "Left" if hand.is_left else "Right"

#         # Choose value based on movement
#         if movement == "Grab Strength":
#             val = hand.grab_strength  # float [0.0–1.0]
#         else:
#             raw = {
#                 "Pitch": hand.direction.pitch,
#                 "Yaw":   hand.direction.yaw,
#                 "Roll":  hand.palm_normal.roll
#             }
#             # convert to degrees
#             val = rad2deg(raw[movement])

#         # Update live metrics
#         rad_ph.metric(f"{movement}",      f"{val:.3f}")
#         deg_ph.metric("Hand Side",        side)
#         hands_ph.metric("Frame Number",   frame.id)

#         # Rolling chart buffer (last 100 points)
#         chart_buffer.append(val)
#         if len(chart_buffer) > 100:
#             chart_buffer.pop(0)
#         chart.add_rows({movement: np.array(chart_buffer)[-1:].reshape(1,)})

#         # Log this data point with timestamp
#         now = datetime.now().isoformat(timespec="milliseconds")
#         log_buffer.append([now, frame.id, movement, side, val])

#     # Flush log_buffer to CSV every 5 seconds
#     if time.time() - last_flush >= 5 and log_buffer:
#         with open(log_file, "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerows(log_buffer)
#         log_buffer.clear()
#         last_flush = time.time()

#     time.sleep(0.03)


# below used distance what used to be in progress reports

import time
import math
import csv
import Leap
import numpy as np
import streamlit as st
from datetime import datetime
import atexit

# ---------------- Setup logging ----------------
start_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"experiment_{start_ts}.csv"
with open(log_file, "w", newline="") as f:
    csv.writer(f).writerow(["timestamp", "frame", "movement", "hand", "value"])
log_buffer = []
last_flush = time.time()

def flush_buffer():
    global log_buffer
    if log_buffer:
        with open(log_file, "a", newline="") as f:
            csv.writer(f).writerows(log_buffer)
        log_buffer.clear()

atexit.register(flush_buffer)

# -------------- Leap + Streamlit Init --------------
rad2deg = lambda r: r * 180.0 / math.pi
controller = Leap.Controller()

st.title("UltraLeap Live Hand‑Tracking Dashboard")

movement = st.selectbox(
    "Select measurement to display",
    ["Pitch", "Yaw", "Roll", "Aperture"]
)

if st.button("🔴 Exit"):
    st.warning("Flushing data and exiting…")
    flush_buffer()
    st.stop()

rad_ph = st.empty()
hand_ph = st.empty()
frame_ph = st.empty()
chart = st.line_chart()
chart_buf = []

# ---------------- Main Loop ----------------
while True:
    try:
        frame = controller.frame()
        hands = frame.hands

        if not hands.is_empty:
            hand = hands[0]
            side = "Left" if hand.is_left else "Right"

            # Choose the right numeric value
            if movement == "Aperture":
                # Gather 5 fingertip positions
                tips = []
                for finger in hand.fingers:  # thumb, index, etc.
                    tp = finger.tip_position
                    tips.append([tp.x, tp.y, tp.z])
                tips_arr = np.array(tips)                       # shape (5,3)
                palm_pos = np.array([                          # shape (3,)
                    hand.palm_position.x,
                    hand.palm_position.y,
                    hand.palm_position.z
                ])
                dists = np.linalg.norm(tips_arr - palm_pos, axis=1)
                val = float(dists.mean())
            else:
                raw = {
                    "Pitch": hand.direction.pitch,
                    "Yaw":   hand.direction.yaw,
                    "Roll":  hand.palm_normal.roll
                }
                val = rad2deg(raw[movement])

            # Live metrics
            rad_ph.metric(f"{movement}", f"{val:.3f}")
            hand_ph.metric("Hand Side", side)
            frame_ph.metric("Frame ID", frame.id)

            # Rolling chart
            chart_buf.append(val)
            if len(chart_buf) > 100:
                chart_buf.pop(0)
            chart.add_rows({movement: np.array(chart_buf)[-1:].reshape(1,)})

            # Log row
            ts = datetime.now().isoformat(timespec="milliseconds")
            log_buffer.append([ts, frame.id, movement, side, val])

        # flush every 5s
        if time.time() - last_flush >= 5 and log_buffer:
            flush_buffer()
            last_flush = time.time()

        time.sleep(0.03)

    except Exception as e:
        st.error(f"Error in loop: {e}")
        break

import time, math
import numpy as np
import streamlit as st
import Leap
import sys
st.write(f"✅ Running with Python {sys.version}")

# Convert radians → degrees
rad2deg = lambda r: r * 180.0 / math.pi

roll_threshold=3
palm_threshold=1.5
PalmUp_val = lambda r: round((90 * (r - palm_threshold) / palm_threshold if r > palm_threshold else 0),2)
PalmDown_val = lambda r: round((90 * (palm_threshold - r) / palm_threshold if r < palm_threshold else 0),2)

# Initialize Leap controller
controller = Leap.Controller()

# Streamlit UI
st.title("UltraLeap Live Hand-Tracking Dashboard")

# Dropdown selector
option = st.selectbox("Select angle to display", ["Roll"])

# Placeholders for metrics
rad_placeholder = st.empty()
deg_placeholder = st.empty()

# Placeholder for Palm Up/Down
palmup_placeholder = st.empty()
palmdown_placeholder = st.empty()

# Line chart setup
chart = st.line_chart()
buffer = []

# Main loop
while True:
    frame = controller.frame()
    hands = frame.hands

    if not hands.is_empty:
        hand = hands[0]
        # raw radian values
        vals_r = {
            "Pitch": hand.direction.pitch,
            "Yaw":   hand.direction.yaw,
            "Roll":  hand.palm_normal.roll
        }
        # convert to degrees
        vals_d = {k: rad2deg(v) for k, v in vals_r.items()}

        # Palm Up/Down calculations
        vals_palm_up = {k: PalmUp_val(v) for k, v in vals_r.items()}
        vals_palm_down = {k: PalmDown_val(v) for k, v in vals_r.items()}

        # get selected
        r = vals_r[option]
        d = vals_d[option]
        palm_up = vals_palm_up[option]
        palm_down = vals_palm_down[option]

        # update metrics
        rad_placeholder.metric(f"{option} (rad)", f"{r:.3f}")
        deg_placeholder.metric(f"{option} (°)",   f"{d:.1f}")
        palmup_placeholder.metric(f"{option} (Palm Up)", f"{palm_up:.1f}")
        palmdown_placeholder.metric(f"{option} (Palm Down)", f"{palm_down:.1f}")

        # update rolling buffer & chart
        buffer.append(d)
        if len(buffer) > 100:
            buffer.pop(0)
        chart.add_rows({option: np.array(buffer)[-1:].reshape(1,)})

    time.sleep(0.03)

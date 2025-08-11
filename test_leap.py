import time, math, Leap

def rad2deg(r): return r * 180.0 / math.pi

ctr = Leap.Controller()
print("Streaming frames… (press Ctrl+C to stop)")

for i in range(50):
    frame = ctr.frame()
    hands = frame.hands
    print(f"Frame {frame.id:5d} — hands detected: {len(hands)}")
    if not hands.is_empty:
        hand = hands[0]
        p, y, r = hand.direction.pitch, hand.direction.yaw, hand.palm_normal.roll
        print(f"  → Pitch: {p:.3f} rad / {rad2deg(p):.1f}°")
        print(f"  → Yaw:   {y:.3f} rad / {rad2deg(y):.1f}°")
        print(f"  → Roll:  {r:.3f} rad / {rad2deg(r):.1f}°")
        break
    time.sleep(0.1)
else:
    print("No hand detected after 50 frames — try adjusting your hand position.")

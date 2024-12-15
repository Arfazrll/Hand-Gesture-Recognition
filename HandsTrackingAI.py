import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,       
    max_num_hands=2,               
    min_detection_confidence=0.5,  
    min_tracking_confidence=0.5    
)

mp_draw = mp.solutions.drawing_utils
FINGER_TIPS = [4, 8, 12, 16, 20]
FINGER_PIPS = [3, 6, 10, 14, 18]

def count_fingers(hand_landmarks, hand_label):
    fingers = []

    if hand_label == "Right":
        if hand_landmarks.landmark[FINGER_TIPS[0]].x < hand_landmarks.landmark[FINGER_PIPS[0]].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else:
        if hand_landmarks.landmark[FINGER_TIPS[0]].x > hand_landmarks.landmark[FINGER_PIPS[0]].x:
            fingers.append(1)
        else:
            fingers.append(0)

    for id in range(1, 5):
        if hand_landmarks.landmark[FINGER_TIPS[id]].y < hand_landmarks.landmark[FINGER_PIPS[id]].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        print("Gagal buka kamera.")
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    total_fingers = 0  
    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            hand_label = hand_info.classification[0].label
            fingers_up = count_fingers(hand_landmarks, hand_label)
            total_fingers += fingers_up
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

    print(f"Jumlah Jari Terangkat: {total_fingers}")
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
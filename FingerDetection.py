import cv2
import mediapipe as mp

# initialize mediapipe hands, read mediapipe hand docs here https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#get_started
  
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

movement_threshold = 0.05 # adjust this value for sensitivity, lower value = less movement needed for detection

# start capturing video from the webcam
# webcam 0 for built in webcam/first webcam, use webcam 1 if we are using external webcam
cap = cv2.VideoCapture(0)

# Previous positions of finger tips for both hands
prev_tips = [{}, {}]  # Two dictionaries, one for each hand

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # mirror view 
    frame = cv2.flip(frame, 1)

    # convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # use mediapipe hands.process on capture to detect fingers
    results = hands.process(rgb_frame)
    
    # index landmark map to readable
    index_to_finger = {
      4 : "Thumb",
      8 : "Index",
      12 : "Middle",
      16 : "Ring",
      20: "Pinky"
    }
  
    # Draw hand landmarks and track fingertips
    if results.multi_hand_landmarks:
        for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for finger_tip_index in [4, 8, 12, 16, 20]:  # Thumb to Pinky tips
                finger_tip = hand_landmarks.landmark[finger_tip_index]

                # Check if the finger tip has moved significantly
                if finger_tip_index in prev_tips[hand_index]:
                    prev_tip = prev_tips[hand_index][finger_tip_index]
                    dx = finger_tip.x - prev_tip.x
                    dy = finger_tip.y - prev_tip.y
                    distance_moved = (dx ** 2 + dy ** 2) ** 0.5
                    
                    if distance_moved > movement_threshold: # if movement > threshold, print detection
                        print(f"Hand {hand_index + 1}, Finger {index_to_finger.get(finger_tip_index)} moved")

                prev_tips[hand_index][finger_tip_index] = finger_tip

    # display the frame
    cv2.imshow('Finger Movement Tracker', frame)

    # use esc key to quit window
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()

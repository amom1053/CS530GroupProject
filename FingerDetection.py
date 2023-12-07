import cv2
import mediapipe as mp
import TestStats
import keyboard

class FingerDetection:
    def __init__(self, sensitivity: int = 0.05):
        # initialize mediapipe hands, read mediapipe hand docs here https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#get_started
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils
        self.movement_threshold = sensitivity  # adjust this value for sensitivity, lower value = less movement needed for detection
        self.cap = None
        self.movementList = []
        self.stopped = False  # Flag to indicate whether the thread should stop

    def startVideoCapture(self, camIndex=0):
        self.cap = cv2.VideoCapture(camIndex)

    def stopGrabbingData(self):
        self.stopped = True

    def startGrabbingData(self):
        # Previous positions of finger tips for both hands
        prev_tips = [{}, {}]  # Two dictionaries, one for each hand

        while not self.stopped:
            ret, frame = self.cap.read()
            if not ret:
                continue

            # mirror view
            frame = cv2.flip(frame, 1)

            # convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # use mediapipe hands.process on capture to detect fingers
            results = self.hands.process(rgb_frame)

            # index landmark map to readable
            index_to_finger = {
                4: "Thumb",
                8: "Index",
                12: "Middle",
                16: "Ring",
                20: "Pinky"
            }

            # Draw hand landmarks and track fingertips
            if results.multi_hand_landmarks:
                for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    for finger_tip_index in [4, 8, 12, 16, 20]:  # Thumb to Pinky tips
                        finger_tip = hand_landmarks.landmark[finger_tip_index]

                        # Check if the finger tip has moved significantly
                        if finger_tip_index in prev_tips[hand_index]:
                            prev_tip = prev_tips[hand_index][finger_tip_index]
                            dx = finger_tip.x - prev_tip.x
                            dy = finger_tip.y - prev_tip.y
                            distance_moved = (dx ** 2 + dy ** 2) ** 0.5

                            if distance_moved > self.movement_threshold:
                                print(f"Hand {hand_index + 1}, Finger {index_to_finger.get(finger_tip_index)} moved")
                                self.movementList.append((hand_index + 1, index_to_finger.get(finger_tip_index)))

                        prev_tips[hand_index][finger_tip_index] = finger_tip

            # Check for Enter key press using keyboard library
            if keyboard.is_pressed('enter'):
                self.stopGrabbingData()

            # Display the frame in the main thread
            cv2.imshow('Finger Movement Tracker', frame)

            # use 'q' key to quit window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the resources
        self.cap.release()
        cv2.destroyAllWindows()

    def getData(self):
        return self.movementList

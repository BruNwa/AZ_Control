import cv2
import math
import time
import faceModule as fm
import handModule as hm
from pynput.keyboard import Key, Controller as KeyboardController, Listener as KeyboardListener
from pynput.mouse import Button, Controller
from threading import Timer
import os
import pyautogui
import numpy as np

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
cap = cv2.VideoCapture(0)
faceDetector = fm.faceModule(trackconf=0.7)
handDetector = hm.handDetector(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mouse = Controller()
keyboard = KeyboardController()

print("Initialization....")
time.sleep(1)
clear_terminal()
print("\n" + "*" * 50)
print(" " * 18 + "AZ CONTROL")
print("*" * 50 + "\n")

print("This application allows you to control your computer using face and hand gestures.")
print("Choose one of the following modes:")
print("1: Control using blink, mouth, and hand gestures.")
print("2: Control the mouse using hand gestures.")
print("3: Exit the application.")


def smooth_move(current_position, target_position, smoothing_factor=0.3):
    return current_position + (target_position - current_position) * smoothing_factor

running = True  

def on_press(key):
    if key == Key.end:
        global running
        running = False  
        return False  
    return True

def exit_program(key):
    global running
    if key.char == 'p':  
        running = False  

def main():
    global running
    listener = KeyboardListener(on_press=on_press)
    listener.start()
    while True:
        choices = input('Please choose from 1-3: ')
        if len(choices) == 1 and choices in ['1', '2', '3']:
            break
        print('Error: Please enter a single character from 1 to 3.')

    if choices == "1":
        print("You have selected mode 1: Control using blink, mouth, and hand gestures.")
        while True:
            show_feed = input("Do you want to display the camera feed? (y/n): ").strip().lower()
            if show_feed == 'y':
                print("ENJOY!!!")
                time.sleep(0.5)
                break
            elif show_feed == 'n':
                print("Remember! to Exit the program click on End button while selecting the terminal.")
                print("ENJOY!!!")
                time.sleep(3)
                break
            print("Error: Please enter 'y' for yes or 'n' for no.")
        clear_terminal()
        while True:
            blink_button = input('Enter the blink control button: ')
            mouth_open = input('Enter the Mouth control button: ')
            handGesture = input('Enter the hand control button: ')
            if len(blink_button) == 1 and len(mouth_open) == 1 and len(handGesture) == 1:
                break
            print('Error: Please enter a single character for each control.')

        hand_gesture_threshold = None
        mouth_open_threshold = None
        blink_threshold = None
        last_update_time = time.time()
        keyboard = KeyboardController()
        last_press_time = 0
    
        while running:
            success, frame = cap.read()
            if not success:
                print('Error: Failed to capture frame')
                break
            
            frame = cv2.flip(frame, 1)

            frame, handPoints = handDetector.findHands(frame, draw=False)
            mesh = faceDetector.facePosition(frame)
            draw_ids = [145, 159, 11, 16]  # Face points IDs
            faceDetector.faceMeshDet(frame, draw_ids)

            if mesh:
                left_eye = [mesh[0][23], mesh[0][27]]
                mouth = [mesh[0][11], mesh[0][16]]
                if left_eye:
                    eye_distance = math.hypot(left_eye[0][2] - left_eye[1][2])
                    current_time = time.time()
                    if blink_threshold is None or (current_time - last_update_time) >= 1:
                        print("Eye Threshold Update...")
                        blink_threshold = eye_distance * 0.9
                        last_update_time = current_time
                    if eye_distance <= blink_threshold and current_time - last_press_time > 1:
                        keyboard.press(blink_button)
                        keyboard.release(blink_button)
                        last_press_time = current_time                  
                if mouth:
                    mouth_distance = math.hypot(mouth[1][2] - mouth[0][2])
                    current_time = time.time()
                    if mouth_open_threshold is None or (current_time - last_update_time) >= 1:
                        print("Mouth Threshold Update...")
                        mouth_open_threshold = mouth_distance * 1.8
                        last_update_time = current_time
                    
                    if mouth_distance > mouth_open_threshold:
                        keyboard.press(mouth_open)
                        keyboard.release(mouth_open)
                        
                        
            if handPoints:
                thumb_tip = handPoints[4]
                index_tip = handPoints[8]
                if thumb_tip and index_tip:
                    hand_distance = math.hypot(thumb_tip[1] - index_tip[1], thumb_tip[2] - index_tip[2])
                    current_time = time.time()
                    if hand_gesture_threshold is None or (current_time - last_update_time) >= 2:
                        print("Gesture Threshold Update...")
                        hand_gesture_threshold = hand_distance * 0.6
                        last_update_time = current_time

                    if hand_distance < hand_gesture_threshold:
                        keyboard.press(handGesture)
                        keyboard.release(handGesture)

            if show_feed == "y":
                cv2.imshow('Control Mode', frame)
            cv2.waitKey(1)
                

    elif choices == '2':
        print("You have selected mode 2: Control the mouse using hand gestures.")
        while True:
            show_feed = input("Do you want to display the camera feed? (y/n): ").strip().lower()
            if show_feed == 'y':
                print("ENJOY!!!")
                time.sleep(0.5)
                break
            elif show_feed == 'n':
                print("Remember! to Exit the program click on End button while selecting the terminal.")
                print("ENJOY!!!")
                time.sleep(3)
                break
            print("Error: Please enter 'y' for yes or 'n' for no.")
        clear_terminal()
        screen_w, screen_h = pyautogui.size()
        current_mouse_x, current_mouse_y = pyautogui.position()
        smoothing_factor = 0.3
        last_click_time = 0
        right_gesture_threshold = None
        left_gesture_threshold = None
        close_gesture_threshold = None
        last_update_time = time.time()
        is_dragging = False
        drag_start_time = 0
        drag_threshold = 0.5 
        
        while running:
            success, frame = cap.read()
            if not success:
                continue
            frame = cv2.flip(frame, 1)  
            frame, handPoints = handDetector.findHands(frame, draw=False)
            if handPoints:
                x, y = handPoints[0][1:]  
                screen_x = np.interp(x, (0, frame.shape[1]), (0, screen_w))
                screen_y = np.interp(y, (0, frame.shape[0]), (0, screen_h))
                current_mouse_x = current_mouse_x * (1 - smoothing_factor) + screen_x * smoothing_factor
                current_mouse_y = current_mouse_y * (1 - smoothing_factor) + screen_y * smoothing_factor
                mouse.position = (int(current_mouse_x), int(current_mouse_y))
                thumb_tip = handPoints[4]
                index_tip = handPoints[8]
                middle_tip = handPoints[12]
                middle_tip2 = handPoints[16]
                pinky_tip = handPoints[20]
                middle_hand = handPoints[0]
                if thumb_tip and index_tip and middle_tip and middle_tip2 and middle_hand and pinky_tip:
                    leftClick = thumb_tip[2] - index_tip[2]
                    rightClick = thumb_tip[2] - middle_tip[2]
                    #closeProgram = math.hypot(middle_hand[2] - middle_tip2[2], middle_hand[2] - pinky_tip[2])
                    current_time = time.time()
                    if left_gesture_threshold is None or (current_time - last_update_time) >= 2:
                        print("Left Gesture Threshold Update...")
                        left_gesture_threshold = leftClick * 0.2
                        last_update_time = current_time
                    if leftClick < left_gesture_threshold:
                        if not is_dragging:
                            if drag_start_time == 0:
                                drag_start_time = current_time
                            elif current_time - drag_start_time > drag_threshold:
                                mouse.press(Button.left)
                                is_dragging = True
                            else:
                                pass
                    else:
                        if is_dragging:
                            mouse.release(Button.left)
                            is_dragging = False
                        else:
                            if drag_start_time != 0 and current_time - drag_start_time <= drag_threshold:
                                mouse.click(Button.left)
                        drag_start_time = 0

                    
                    if right_gesture_threshold is None or (current_time - last_update_time) >= 2:
                        print("Right Gesture Threshold Update...")
                        right_gesture_threshold = rightClick * 0.2
                        last_update_time = current_time
                    if rightClick < right_gesture_threshold and current_time - last_click_time > 1:
                        mouse.click(Button.right)
                        last_click_time = current_time
                      
                    #if close_gesture_threshold is None or (current_time - last_update_time) >= 2:
                        #close_gesture_threshold = closeProgram * 0.2
                        #last_update_time = current_time
                    #if closeProgram < close_gesture_threshold:
                        #KeyboardController.press(key=Key.end)
                        #KeyboardController.release(key=Key.end)

                        
                        
            if show_feed == "y":
                cv2.imshow('Mouse Mode', frame) 
            cv2.waitKey(1) 
                

    elif choices == '3':
        print("Exiting the program.")
        running = False  
        return
    listener.join() 

try:
    main()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
finally:
    cap.release()
    cv2.destroyAllWindows()
